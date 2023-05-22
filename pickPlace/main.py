import argparse
import sys
import pandas as pd
import re
from tqdm import tqdm
sys.path.append('../')

from asp_modules import action, DEC_AXIOMS
from asp_domains import block_world
from pipeline import Pipeline

def parse_answer_set(answer_set):
    plan = ''
    # find the ordered list of actions
    # actions = [atom.replace('pick_and_place(', '')[:-1] for atom in answer_set if atom.startswith('pick_and_place')]
    # actions = [s.replace('\"','').split(',') for s in actions]
    actions = [atom.replace('happens(action(robot,pick_and_place,', '')[:-1]
        for atom in answer_set if atom.startswith('happens(action(robot,pick_and_place')]
    actions = [s.replace('\")','').replace('\"','').split(',') for s in actions]
    actions.sort(key=lambda x: int(x[-1]))
    for i, action in enumerate(actions):
        plan += f'{i+1}. Move the {action[0]} onto the {action[1]}.\n'
    return plan.strip()

class BlockWorld(Pipeline):
    # take a dataset file in csv and return #correct and #total
    def eval_dataset(self, path_to_dataset, max_num=None):
        correct = 0
        total = 0
        # find the hyperparameters in the dataset
        m = re.search('maxHeight=(\d+)_', path_to_dataset)
        assert m, 'Error: cannot find maxHeight=X_ from the file name'
        max_height = int(m.group(1))
        stack_fact = f'#const max_height={max_height}.\n'
        # read in the dataset
        df = pd.read_csv(path_to_dataset, sep='\t', encoding='utf-8')
        for _, row in tqdm(df.iterrows(), total=df.shape[0]):
            # all labels are stored in sentences format in short_plans
            short_plans, sol = row['short plans'], 0
            # each example is a mapping from kind (str) to list of sentences (str)
            example = {kind: [] for kind in ('init', 'goal')}
            for kind in ('init', 'goal'):
                sentences = row[f'{kind} state'].split('\n')
                example[kind] = [s for s in sentences if not s.startswith('Nothing')]
            answer_sets, response = self.eval_single_example(example, stack_fact, opt=True)            
            # we choose the first answer set as the final prediction
            if answer_sets:
                predicted_plan = parse_answer_set(answer_sets[0])
                sol = 1 if predicted_plan in short_plans else 0
            correct += sol
            total += 1
            # record the mistake
            if sol == 0:
                if self.debug:
                    breakpoint()
                self.mistakes.append((
                    path_to_dataset,
                    total,
                    '# Initial State:\n' + row['init state'] + '\n# Goal State:\n' + row['goal state'],
                    short_plans,
                    response.replace('.', '.\n')[:-1]))
            if max_num and total == max_num:
                break
        return correct, total

def main(args):
    pipeline = BlockWorld(vars(args))
    # 1. Set up the ASP program
    pipeline.asp_program = block_world + action + DEC_AXIOMS
    # 2. Load the prompt
    path_prompt = {kind: f'prompts/{kind}_state.txt' for kind in ('init', 'goal')}
    pipeline.load_prompt(path_prompt)
    # 3. Load the cache for GPT-3 response to avoid duplicated query
    pipeline.path_cache = {
        kind: f'cached_responses/{kind}_{pipeline.engine}.pickle'
        for kind in ('init', 'goal')}
    pipeline.load_cache()
    # 4. Evaluate on test data
    max_num = args.num # maximum number of data to be evaluated per file
    path_test_data_files = [
        'data/numData=20_minStack=3_bowl=True_minSteps=3_maxHeight=2_seed=0.csv',
        'data/numData=20_minStack=1_bowl=False_minSteps=3_maxHeight=7_seed=0.csv',
    ]
    correct = total = 0
    print('acc\tcorrect\ttotal\tfile_name')
    for file in path_test_data_files:
        _correct, _total = pipeline.eval_dataset(file, max_num)
        print(f'{100*_correct/_total:.2f}\t{_correct}\t{_total}\t{file}')
        correct += _correct
        total += _total
    print(f'{100*correct/total:.2f}\t{correct}\t{total}\tAll')

    # 5. record the mistakes
    mistake_cols = ['file', 'index', 'example', 'target', 'response']
    pipeline.save_mistakes(mistake_cols)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--num', default=-1, type=int,
        help='maximum number of data to be evaluated per file; -1 means all data')
    parser.add_argument('--engine', default='text-davinci-003', type=str,
        help='the engine name in \{text-davinci-003, text-davinci-002, text-curie-001\}')
    parser.add_argument('--path_mistakes', default='mistakes.xlsx', type=str,
        help='the file that records mistakes')
    parser.add_argument('--debug', default=False, action='store_true', help='debug mode')
    args = parser.parse_args()
    main(args)
