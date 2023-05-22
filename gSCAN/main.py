import argparse
import json
import sys
sys.path.append('../')

from tqdm import tqdm
from asp_modules import action, DEC_AXIOMS
from asp_domains import gscan
from pipeline import Pipeline

direction_map = {
    0: 'east',
    1: 'south',
    2: 'west',
    3: 'north'
}

def parse_data(data):
    example = {}
    example['goal'] = [data['command']]
    target = data['target_commands'].replace('turn ', 'turn_')
    situation = data['situation']
    facts = ''
    facts += 'gridSize(' + str(situation['grid_size']) + ').\n'
    x, y = situation['agent_position']['row'], situation['agent_position']['column']
    direction = direction_map[situation['agent_direction']]
    facts += f'pos(agent, ({x},{y})).\n' + f'dir(agent, {direction}).\n'
    for idx in situation['placed_objects']:
        info = situation['placed_objects'][idx]
        x, y = info['position']['row'], info['position']['column']
        facts += f'\npos({idx}, ({x},{y})).\n'
        for feature in info['object']:
            value = info['object'][feature]
            facts += f'{feature}({idx}, {value}).\n'
    # determine the splits of the example according to the gSCAN paper
    splits = ''
    # Experiment B: visual generalization. yellow square in command
    if 'yellow' in data['command'] and 'square' in data['command']:
        splits += 'B'
    # Experiment C: visual generalization. target is red square
    if situation['target_object']['object']['color'] == 'red' and \
        situation['target_object']['object']['shape'] == 'square':
        splits += 'C'
    # Experiment D: situational generalization, hold out all directions of agent to target = South-West.
    if situation['direction_to_target'] == 'sw':
        splits += 'D'
    # Experiment E: situational generalization, hold out all situations where a circle of size 2 is referred to
    # as the small circle.
    if 'small' in data['referred_target'] and \
        situation['target_object']['object']['shape'] == 'circle' and \
        situation['target_object']['object']['size'] == '2':
        splits += 'E'
    # Experiment F: contextual generalization, hold out all situations where interaction with a red square of
    # size 3 is required.
    if 'push' in data['command'] and \
        situation['target_object']['object']['shape'] == 'square' and \
        situation['target_object']['object']['size'] == '3':
        splits += 'F'
    # Experiment G: generalize adverb to new situations.
    if 'cautiously' in data['command']:
        splits += 'G'
    # Experiment H: generalize adverb to new verb 'pull'.
    if 'pull' in data['command'] and 'while spinning' in data['command']:
        splits += 'H'
    return example, target, facts, splits

class GSCAN(Pipeline):
    # return the answer sets for an example data instance
    def eval_single_example(self, example, facts='', limit=120, clean=False):
        """
        Args:
            example (dict): a mapping from kind (str) to a list of sentences
            facts (str): additionally facts used during inference
            limit (int): the limit on the max timestamp considered during inference
            clean (bool): if true, remove all quotes turn all letters into lower case
        """
        response = ''
        for kind in example:
            for sentence in example[kind]:
                response += self.gen_response(sentence, kind)
        if clean:
            response = response.replace('\"', '').lower()
        maxtime, answer_sets = 20, []
        while not answer_sets and maxtime <= limit:
            fact = f'maxtime({maxtime}).\n'
            answer_sets = self.gen_answer_set(response + facts + fact, opt=True)
            maxtime += 20
        return answer_sets, response

    def parse_answer_sets(self, answer_sets):
        answer_sets = [[atom for atom in model if atom.startswith('happens')] for model in answer_sets]
        predictions = []
        for atoms in answer_sets:
            actions = [atom.replace('happens(action(agent,', '')[:-1] for atom in atoms]
            actions = [s.split('),') for s in actions]
            actions.sort(key=lambda x: int(x[1]))
            predictions.append(','.join([action for action,_ in actions]))
        return predictions

    # take a dataset file in txt and return #correct and #total
    def eval_dataset(self, path_to_dataset, max_num=None):
        # prepare counters for each split
        self.split_categories = {'test': 'A', 'visual_easier': 'B', 'visual': 'C', 'situational_1': 'D',
            'situational_2': 'E', 'contextual': 'F', 'adverb_1': 'G', 'adverb_2': 'H'}
        correct, total = {}, {}
        for cat in self.split_categories:
            correct[cat], total[cat] = 0, 0
        # read in the dataset
        with open(path_to_dataset, 'r') as f:
            dataset = json.load(f)
        if self.debug:
            print('Keys in dataset: ', dataset.keys())
            print('Keys in dataset[\'examples\']: ', dataset['examples'].keys())
            print('Number of test data: ', len(dataset['examples']['test']))
        # enumerate each test data split
        for cat in dataset['examples']:
            if cat in self.split_categories:
                for idx, data in enumerate(tqdm(dataset['examples'][cat])):
                    if idx == max_num:
                        break
                    example, target, facts, splits = parse_data(data)
                    # print(self.split_categories[cat], data['command'], '===', splits)
                    answer_sets, response = self.eval_single_example(example, facts=facts)
                    predictions = self.parse_answer_sets(answer_sets)
                    total[cat] += 1
                    if target in predictions:
                        correct[cat] += 1
                    else:
                        # print(target)
                        # print('\n'.join(example['goal']))
                        # print(response)
                        # breakpoint()
                        self.mistakes.append((
                            path_to_dataset,
                            self.split_categories[cat] + f' {idx}',
                            target,
                            '\n'.join(example['goal']),
                            response + '\n\n' + facts))
                accuracy = 100*correct[cat]/total[cat] if total[cat] else 0
                print(f'{self.split_categories[cat]}\t{accuracy:.2f}\t{correct[cat]}\t{total[cat]}')
        return correct, total

def main(args):
    pipeline = GSCAN(vars(args))
    # 1. Set up the ASP program
    pipeline.asp_program = gscan + action + DEC_AXIOMS
    # 2. Load the prompt
    path_prompt = {'goal': 'prompt_goal.txt'}
    pipeline.load_prompt(path_prompt)
    # 3. Load the cache for GPT-3 response to avoid duplicated query
    pipeline.path_cache = {'goal': f'cached_responses/cache_{pipeline.engine}.pickle'}
    pipeline.load_cache()
    # 4. Evaluate on test data
    max_num = args.num # maximum number of data to be evaluated per file
    path_test_data_files = [
        'data/compositional_splits/dataset.txt'
    ]
    correct = total = 0
    for file in path_test_data_files:
        _correct, _total = pipeline.eval_dataset(file, max_num)
        print('Split\tComment\t\tAcc\tCorrect\tTotal\tFile name')
        for cat in pipeline.split_categories:
            accuracy = 100*_correct[cat]/_total[cat] if _total[cat] else 0
            print(f'{pipeline.split_categories[cat]}\t{cat:15s}\t{accuracy:.2f}\t{_correct[cat]}\t{_total[cat]}\t{file}')
            correct += _correct[cat]
            total += _total[cat]
    print(f'all\t{100*correct/total:.2f}\t{correct}\t{total}\tAll')

    # 5. record the mistakes
    mistake_cols = ['file', 'index', 'target', 'example', 'response']
    pipeline.save_mistakes(mistake_cols)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--num', default=20, type=int,
        help='maximum number of data to be evaluated per file')
    parser.add_argument('--engine', default='text-curie-001', type=str,
        help='the engine name in \{text-davinci-002, text-curie-001\}')
    parser.add_argument('--path_mistakes', default='mistakes.xlsx', type=str,
        help='the file that records mistakes')
    parser.add_argument('--debug', default=False, action='store_true', help='debug mode')
    args = parser.parse_args()
    main(args)