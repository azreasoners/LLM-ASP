import argparse
from collections import defaultdict
import sys
import pandas as pd
from tqdm import tqdm
sys.path.append('../')

from pipeline import Baseline

class StepGame(Baseline):
    # take a dataset file in csv and return #correct and #total
    def eval_dataset(self, path_to_dataset, max_num=None):
        correct, total = defaultdict(int), 0
        # read in the dataset
        with open(path_to_dataset, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        # read in the dataset
        df = pd.read_csv(path_to_dataset, sep='\t', encoding='utf-8')
        
        for _, row in tqdm(df.iterrows(), total=df.shape[0]):
            # all labels are stored in sentences format in short_plans
            short_plans = row['short plans']
            # form the [INPUT] for this example
            inp = '# Initial State:\n[I1]\n\n# Goal State:\n[I2]'
            inp = inp.replace('[I1]', row['init state']).replace('[I2]', row['goal state'])
            # each example is a mapping from name (str) to sentences (str)
            example = {name: inp for name in self.prompt}
            response = self.eval_single_example(example)
            total += 1
            for name in response:
                sol = 1 if response[name] in short_plans else 0
                correct[name] += sol
                # record the mistake
                if sol == 0:
                    if self.debug:
                        breakpoint()
                    self.mistakes.append((
                        path_to_dataset,
                        total,
                        inp,
                        short_plans,
                        name,
                        response[name]))
            if max_num and total == max_num:
                break
    #     return correct, total
    
    # take a dataset file in csv and return #correct and #total
    def eval_dataset(self, path_to_dataset, max_num=None):
        correct, total = defaultdict(int), 0
        # read in the dataset
        with open(path_to_dataset, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        # each example is a mapping from name (str) to [INPUT] sentences (str)
        inp = ''
        for line in lines:
            _, line = line.strip().split(' ', 1)
            if line.endswith('1'):
                line, target, _ = line.split('\t')
                inp += line
                example = {name: inp for name in self.prompt}
                response = self.eval_single_example(example)
                total += 1
                for name in response:
                    prediction = response[name].split(' ')[-1] if name == 'base_CoT' else response[name]
                    sol = 1 if target in prediction else 0
                    correct[name] += sol
                    # record the mistake
                    if sol == 0:
                        if self.debug:
                            breakpoint()
                        self.mistakes.append((
                            path_to_dataset,
                            total,
                            inp,
                            target,
                            name,
                            response[name]))
                inp = ''
            else:
                inp += line + '\n'
            if max_num and total == max_num:
                break
        return correct, total

def main(args):
    pipeline = StepGame(vars(args))
    # 1. Load the prompt, which we call base
    # (one can test multiple versions of prompts by adding, e.g., 'base2': PATH)
    path_prompt = {
        'base': 'prompts/baseline.txt',
        'base_CoT': 'prompts/baseline_CoT.txt',
        }
    pipeline.load_prompt(path_prompt)
    # 2. Load the cache for GPT-3 response to avoid duplicated query
    pipeline.path_cache = {
        name: f'cached_responses/{name}_{pipeline.engine}.pickle'
        for name in path_prompt}
    pipeline.load_cache()
    # 3. Evaluate on test data
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
    correct, total = defaultdict(int), 0
    print('name    \tacc\tcorrect\ttotal\tfile_name')
    for file in path_test_data_files:
        _correct, _total = pipeline.eval_dataset(file, max_num)
        for name in pipeline.prompt:
            print(f'{name: <8}\t{100*_correct[name]/_total:.2f}\t{_correct[name]}\t{_total}\t{file}')
            correct[name] += _correct[name]
        total += _total
    for name in pipeline.prompt:
        print(f'{name: <8}\t{100*correct[name]/total:.2f}\t{correct[name]}\t{total}\tAll')

    # 5. record the mistakes
    mistake_cols = ['file', 'index', 'example', 'target', 'prompt name', 'response']
    pipeline.save_mistakes(mistake_cols)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--num', default=100, type=int,
        help='maximum number of data to be evaluated per file')
    parser.add_argument('--engine', default='text-davinci-003', type=str,
        help='the engine name in \{text-davinci-003, text-davinci-002, text-curie-001\}')
    parser.add_argument('--path_mistakes', default='mistakes.xlsx', type=str,
        help='the file that records mistakes')
    parser.add_argument('--debug', default=False, action='store_true', help='debug mode')
    args = parser.parse_args()
    main(args)
