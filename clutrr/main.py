import argparse
import sys
sys.path.append('../')
import pandas as pd
from tqdm import tqdm
from asp_modules import family
from pipeline import Pipeline

class CLUTRR(Pipeline):
    # take a dataset file in csv and return #correct and #total
    def eval_dataset(self, path_to_dataset, rel_name, max_num=None):
        correct = 0
        total = 0
        # read in the dataset
        df = pd.read_csv(path_to_dataset)
        for _, row in tqdm(df.iterrows(), total=df.shape[0]):
            total += 1
            # each example is a mapping from kind (str) to list of sentences (str)
            example = {rel_name: [row['story'].strip()], 'gender': [row['story'].strip()]}
            # NOTE: a simple cleaning on GPT-3 responses doesn't improve the accuracy
            # clean = self.engine == 'text-curie-001'
            clean = False
            answer_sets, response = self.eval_single_example(example, clean=clean)
            # check if the prediction is correct
            person1, person2 = eval(row['query'])
            target = row['target'].replace('neice', 'niece')
            target_atom = f'{target}(\"{person1}\",\"{person2}\")'.replace('-', '_')
            if clean:
                target_atom = target_atom.replace('\"', '').lower()
            sol = 1 if any([target_atom in answer_set for answer_set in answer_sets]) else 0
            correct += sol
            if sol == 0:
                # record the mistake
                self.mistakes.append((
                    path_to_dataset,
                    total,
                    target_atom,
                    '\n'.join(example[rel_name]),
                    response.replace('.', '.\n')[:-1]
                    ))
            if max_num and total == max_num:
                break
        return correct, total

def main(args):
    pipeline = CLUTRR(vars(args))
    # 1. Set up the ASP program
    pipeline.asp_program = family
    # 2. Load the prompt
    if pipeline.dataset == 'clutrr_s':
        dataset, rel_name = 'CLUTRR-S', 'relation_same_order'
        if args.oppo:
            rel_name = 'relation'
    else:
        dataset, rel_name = 'CLUTRR', 'relation2'
        if args.oppo:
            # rel_name = 'relation_opposite_order'
            rel_name = 'relation2_opposite_order'
    path_prompt = {
        rel_name: f'prompts/{dataset}_{rel_name}.txt',
        'gender': f'prompts/{dataset}_gender.txt'
        }
    pipeline.load_prompt(path_prompt)
    # 3. Load the cache for GPT-3 response to avoid duplicated query
    pipeline.path_cache = {
        rel_name: f'cached_responses/{dataset}_{rel_name}_{pipeline.engine}.pickle',
        'gender': f'cached_responses/{dataset}_gender_{pipeline.engine}.pickle',
        }
    pipeline.load_cache()
    # 4. Evaluate on test data
    max_num = None # maximum number of data to be evaluated per file
    path_test_data_files = [
        # CLUTRR [train=clean]
        'data/clutrr/data_7c5b0e70/1.2_test.csv', # clean
        'data/clutrr/data_7c5b0e70/1.3_test.csv', # clean
        'data/clutrr/data_7c5b0e70/2.3_test.csv', # supporting
        'data/clutrr/data_7c5b0e70/3.3_test.csv', # irrelevant
        'data/clutrr/data_7c5b0e70/4.3_test.csv', # disconnected
        # CLUTRR [train=supporting]
        'data/clutrr/data_06b8f2a1/2.2_test.csv', # supporting
        'data/clutrr/data_06b8f2a1/2.3_test.csv', # supporting
        # CLUTRR [train=irrelevant]
        'data/clutrr/data_523348e6/3.2_test.csv', # irrelevant
        'data/clutrr/data_523348e6/3.3_test.csv', # irrelevant
        # CLUTRR [train=disconnected]
        'data/clutrr/data_d83ecc3e/4.2_test.csv', # disconnected
        'data/clutrr/data_d83ecc3e/4.3_test.csv', # disconnected

        # CLUTRR-S [train=clean]
        'data/clutrr_s/deepproblog_data_2d5007e7/1.2_test.csv', # clean
        'data/clutrr_s/deepproblog_data_2d5007e7/1.3_test.csv', # clean
        'data/clutrr_s/deepproblog_data_2d5007e7/2.3_test.csv', # supporting
        'data/clutrr_s/deepproblog_data_2d5007e7/3.3_test.csv', # irrelevant
        'data/clutrr_s/deepproblog_data_2d5007e7/4.3_test.csv', # disconnected
        # CLUTRR-S [train=supporting]
        'data/clutrr_s/deepproblog_data_a7d9402e/2.2_test.csv', # supporting
        'data/clutrr_s/deepproblog_data_a7d9402e/2.3_test.csv', # supporting
        # CLUTRR-S [train=irrelevant]
        'data/clutrr_s/deepproblog_data_6b1c2f15/3.2_test.csv', # irrelevant
        'data/clutrr_s/deepproblog_data_6b1c2f15/3.3_test.csv', # irrelevant
        # CLUTRR-S [train=disconnected]
        'data/clutrr_s/deepproblog_data_47b0ffea/4.2_test.csv', # disconnected
        'data/clutrr_s/deepproblog_data_47b0ffea/4.3_test.csv', # disconnected

        # CLUTRR 1.3
        'data/clutrr_1.3/clean_100.csv', # clean
        'data/clutrr_1.3/supporting_100.csv', # supporting
        'data/clutrr_1.3/irrelevant_100.csv', # irrelevant
        'data/clutrr_1.3/disconnected_100.csv', # disconnected

        # CLUTRR 1.3 (cleaned version)
        'data/clutrr_1.3_clean/clean_100.csv', # clean
        'data/clutrr_1.3_clean/supporting_91.csv', # supporting
        'data/clutrr_1.3_clean/irrelevant_95.csv', # irrelevant
        'data/clutrr_1.3_clean/disconnected_98.csv', # disconnected
    ]
    correct = total = 0
    print('acc\tcorrect\ttotal\tfile_name')
    for file in path_test_data_files:
        # filter in the dataset files in the corresponding dataset
        if pipeline.dataset + '/' in file:
        # if pipeline.simple == ('deepproblog' in file):
            _correct, _total = pipeline.eval_dataset(file, rel_name, max_num)
            print(f'{100*_correct/_total:.2f}\t{_correct}\t{_total}\t{file}')
            correct += _correct
            total += _total
    print(f'{100*correct/total:.2f}\t{correct}\t{total}\tAll')

    # 5. record the mistakes
    mistake_cols = ['file', 'index', 'target', 'example', 'response']
    pipeline.save_mistakes(mistake_cols)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset', default='clutrr', type=str,
        help='the dataset name in \{clutrr, clutrr_1.3, clutrr_1.3_clean, clutrr_s\}')
    parser.add_argument('--engine', default='text-davinci-002', type=str,
        help='the engine name in \{text-davinci-003, text-davinci-002, text-curie-001\}')
    parser.add_argument('--path_mistakes', default='mistakes.xlsx', type=str,
        help='the file that records mistakes')
    parser.add_argument('--debug', default=False, action='store_true', help='debug mode')
    parser.add_argument('--oppo', default=False, action='store_true',
        help='Ablation study on the prompt with opposite order of arguments')
    args = parser.parse_args()
    main(args)