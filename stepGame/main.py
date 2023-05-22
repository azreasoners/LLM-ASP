import argparse
import sys
sys.path.append('../')

from asp_modules import location
from asp_domains import stepgame
from pipeline import Pipeline

class StepGame(Pipeline):
    target_map = {
        'above': 'top',
        'below': 'down',
        'left': 'left',
        'right': 'right',
        'upper-left': 'top_left',
        'upper-right': 'top_right',
        'lower-left': 'down_left',
        'lower-right': 'down_right'
        }

    # take a dataset file in csv and return #correct and #total
    def eval_dataset(self, path_to_dataset, max_num=None):
        correct = 0
        total = 0
        # read in the dataset
        with open(path_to_dataset, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        # each example is a mapping from kind (str) to list of sentences (str)
        example = {'location': []}
        for line in lines:
            _, line = line.strip().split(' ', 1)
            if line.endswith('1'):
                line, target, _ = line.split('\t')
                target_atom = f'answer({self.target_map.get(target, target)})'
                example['location'].append(line)
                clean = self.engine == 'text-curie-001'
                answer_sets, response = self.eval_single_example(example, clean=clean)
                sol = 1 if any([target_atom in answer_set for answer_set in answer_sets]) else 0
                correct += sol
                total += 1
                # record the mistake
                if sol == 0:
                    self.mistakes.append((
                        path_to_dataset,
                        total,
                        target,
                        '\n'.join(example['location']),
                        response.replace('.', '.\n')[:-1]))
                example = {'location': []}
            else:
                example['location'].append(line)
            if max_num and total == max_num:
                break
        return correct, total

def main(args):
    pipeline = StepGame(vars(args))
    # 1. Set up the ASP program
    pipeline.asp_program = stepgame + location
    # 2. Load the prompt
    path_prompt = {'location': 'prompts/location.txt'}
    pipeline.load_prompt(path_prompt)
    # 3. Load the cache for GPT-3 response to avoid duplicated query
    pipeline.path_cache = {'location': f'cached_responses/location_{pipeline.engine}.pickle'}
    pipeline.load_cache()
    # 4. Evaluate on test data
    max_num = args.num # maximum number of data to be evaluated per file
    path_test_data_files = [
        'data/noise/qa1_test.txt',
        'data/noise/qa2_test.txt',
        'data/noise/qa3_test.txt',
        'data/noise/qa4_test.txt',
        'data/noise/qa5_test.txt',
        'data/noise/qa6_test.txt',
        'data/noise/qa7_test.txt',
        'data/noise/qa8_test.txt',
        'data/noise/qa9_test.txt',
        'data/noise/qa10_test.txt',
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
    mistake_cols = ['file', 'index', 'target', 'example', 'response']
    pipeline.save_mistakes(mistake_cols)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--num', default=1000, type=int,
        help='maximum number of data to be evaluated per file')
    parser.add_argument('--engine', default='text-davinci-002', type=str,
        help='the engine name in \{text-davinci-002, text-curie-001\}')
    parser.add_argument('--path_mistakes', default='mistakes.xlsx', type=str,
        help='the file that records mistakes')
    parser.add_argument('--debug', default=False, action='store_true', help='debug mode')
    args = parser.parse_args()
    main(args)
