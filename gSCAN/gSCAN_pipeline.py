import argparse
import sys
sys.path.append('../')

from clingo.control import Control
import pandas as pd

from asp_modules import action, DEC_AXIOMS
from asp_domains import gscan

class gSCAN:
    def __init__(self):
        self.asp_program = gscan + action + DEC_AXIOMS
        # data
        self.colnames = ['query', 'target', 'asp_grid', 'asp_query'] 
        self.path_test_data = [
            # 'data/walk_100.csv',
            # 'data/walk_caut_100.csv', # (something wrong)
            # 'data/walk_hesitant_100.csv', # Response lacks while(hesitantly)
            # 'data/walk_spinning_100.csv', # (a wrong atom "while")
            'data/walk_zig_100.csv',
            # 'data/push_100.csv',
            # 'data/push_caut_100.csv',
            # 'data/push_hesitant_100.csv',
            # 'data/push_spinning_100.csv',
            # 'data/push_zig_100.csv',
            # 'data/pull_100.csv',
            # 'data/pull_caut_100.csv',
            # 'data/pull_hesitant_100.csv',
            # 'data/pull_spinning_100.csv',
            # 'data/pull_zig_100.csv',
        ]
        # store the wrong predictions
        self.mistakes = []
    
    # take a GPT3 response and return the answer set
    def gen_answer_sets(self, response):
        program = self.asp_program + response
        clingo_control = Control(['0', '--warn=none', '--opt-mode=optN', '-t', '4'])
        answer_sets = []
        try:
            clingo_control.add('base', [], program)
        except:
            breakpoint()
        clingo_control.ground([('base', [])])
        clingo_control.solve(on_model = lambda model: 
            answer_sets.append(model.symbols(atoms=True)) if model.optimality_proven else None)
        answer_sets = [[str(atom) for atom in model] for model in answer_sets]
        return answer_sets
    
    # take a GPT3 response and find the answer set where the time horizon
    # is dymanically increased until an answer set is found or it exceeds a limit
    def gen_answer_sets_dynamic(self, response, limit=80):
        maxtime = 0
        answer_sets = []
        while not answer_sets:
            maxtime += 20
            if maxtime > limit:
                break
            fact = f'maxtime({maxtime}).\n'
            answer_sets = self.gen_answer_sets(fact + response)
        return answer_sets

    def parse_answer_sets(self, answer_sets):
        answer_sets = [[atom for atom in model if atom.startswith('happens')] for model in answer_sets]
        predictions = []
        for atoms in answer_sets:
            actions = [atom.replace('happens(action(agent,', '')[:-1] for atom in atoms]
            actions = [s.split('),') for s in actions]
            actions.sort(key=lambda x: int(x[1]))
            predictions.append(','.join([action for action,_ in actions]))
        return predictions

    def eval_csv(self, path_data):
        df = pd.read_csv(path_data, names=self.colnames, header=None)
        total = correct = 0
        to_check = [54, 93, 95, 96]
        for idx, row in df.iterrows():
            # if idx not in to_check:
            #     continue
            # breakpoint()
            target = row['target'].replace('turn ', 'turn_')
            response = ''
            for colname in self.colnames:
                if 'asp' in colname:
                    response += row[colname]
            predictions = self.parse_answer_sets(self.gen_answer_sets_dynamic(response))
            total += 1
            if target in predictions:
                correct += 1
                # row['predictions'] = predictions
                # row['correct'] = 1
                # self.mistakes.append((row))
            else:
                print(row['query'])
                print(row['target'])
                print('num of steps:', len(target.split(',')))
                breakpoint()
                print(response)
                row['predictions'] = predictions
                row['correct'] = 0
                self.mistakes.append((row))
        return total, correct
    
    def test(self):
        print('Correct\tTotal\tAccuracy\tPath')
        for path in self.path_test_data:
            total, correct = self.eval_csv(path)
            print(f'{correct}\t{total}\t{100*correct/total:.2f}\t{path}')
    
    def save_mistakes(self, path_mistakes):
        df = pd.DataFrame(self.mistakes, columns=self.colnames + ['predictions', 'correct'])
        df.to_excel(path_mistakes)



def main(args):
    pipeline = gSCAN()
    pipeline.test()
    pipeline.save_mistakes(args.path_mistakes)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--debug', default=False, action='store_true', help='debug mode')
    parser.add_argument('--path_mistakes', default='mistakes.xlsx', type=str,
        help='the file that records mistakes')
    args = parser.parse_args()
    main(args)