import argparse

from clingo.control import Control
from clingo.symbol import parse_term
import pandas as pd
import random

block_world = '''
%%%%%
% Set up the environment
%%%%%

% Define the number of grippers for the robot
#const grippers=1.

% Define the maximum number of steps to consider
{maxstep(M): M=0..10} = 1.
step(T) :- maxstep(M), T=0..M.
astep(T) :- maxstep(M), T=0..M-1.
:~ maxstep(M). [M]

% Define all locations
location(table).
location(L) :- feature(L, block).
location(L) :- feature(L, bowl).

%%%%%
% Extract the features for all items in the intial and goal states
% we assume these items form the complete set of items in this example
%%%%%

feature(I, F) :- on(I,_), F=@gen_feature(I).
feature(I, F) :- on(I,_,0), F=@gen_feature(I).
feature(I, F) :- on(_,I), I!=table, F=@gen_feature(I).
feature(I, F) :- on(_,I,0), I!=table, F=@gen_feature(I).

%%%%%
% Define the states and actions in Block World
%%%%%

% **** 1. states -- on(B,L,T) ****

% Initially every bowl is on the table
on(I,table,0) :- feature(I, bowl).

% Commonsense law of inertia
% If an item I is on location L at time T, it is possible to remain on L at T+1
{on(I,L,T+1)} :- on(I,L,T), astep(T).

% At any time T, no item can be on itself
:- on(I,I,T).

% Uniqueness and Existence of state values
% At any time T, each item I can only be on (exact) 1 location
:- step(T), feature(I,_), not 1{on(I,L,T): location(L)}1.

% At any time T, for each block/bowl, there cannot be 2 items directly on it
:- step(T), feature(B, _), 2{on(I,B,T): feature(I,_)}.

% Initially, there must be at least one item on the table (prune out the case of a loop: 1 on 2 on 3 on 4 on 5 on 6 on 1)
:- not 1{on(I,table,0): feature(I,_)}.

% **** 2. action -- pick_and_place(B,L,T) ****

% Actions are exogenous
% At any action step T, we can pick_and_place a block onto any location. But the number of movement is bounded by the number of grippers
{pick_and_place(I,L,T): feature(I,block), location(L)}grippers :- astep(T).

% Effect of pick_and_place an item
on(I,L,T+1) :- pick_and_place(I,L,T).

% An item cannot be moved if there is another item on it
% NOTE: it depends on the domain and might be possible to move a bowl with blocks in it
:- pick_and_place(I,L,T), on(_,I,T).

% An item can’t be moved onto another item that is being moved also
:- pick_and_place(I,I1,T), pick_and_place(I1,_,T).

% **** 3. goal -- on(A,B) ****

:- on(A,B), maxstep(M), not on(A,B,M).

% **** 4. constraints ****

% if there are bowls on the table, a block can only be on a block or a bowl
:- feature(_,bowl), feature(I,block), on(I,L,_), {feature(L, block); feature(L, bowl)} = 0.

% there cannot be more than max_height-1 blocks on a block
up(A,B,T) :- on(A,B,T).
up(A,C,T) :- up(A,B,T), up(B,C,T).
:- step(T), feature(L, block), #count{I: up(I,L,T)} >= max_height.
'''

class Context:
    def gen_feature(self, x):
        ret = []
        for term in str(x.string).split(' '):
            ret.append(parse_term(term))
        return ret

class BlockWorldData:
    def __init__(self):
        self.rainbow_colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
        self.sort_order = {}
        for i in range(len(self.rainbow_colors)):
            self.sort_order[self.rainbow_colors[i] + ' block'] = i
        self.column_names = [
            'init state', 'goal state', 'short plans', 'long plan',
            'number of bowls/stacks', 'number of blocks', 'number of steps',
            'init state(ASP)', 'goal state(ASP)'
            ]
        self.asp_program = block_world
    
    def interpret_state(self, state):
        """
        Args:
            state: a list of stacks, each stack is a list of str (for objects)
        """
        state_sentence = state_asp = ''
        state = [stack for stack in state if stack]
        for stack in state:
            if 'bowl' not in stack[0]:
                state_sentence += f'The {stack[0]} is on the table.\n'
                state_asp += f'on(\"{stack[0]}\", table).\n'
            elif len(stack) == 1:
                state_sentence += f'Nothing is on the {stack[0]}.\n'
            for i in range(1, len(stack)):
                state_sentence += f'The {stack[i]} is on the {stack[i-1]}.\n'
                state_asp += f'on(\"{stack[i]}\", \"{stack[i-1]}\").\n'
        return state_sentence.strip(), state_asp
    
    def gen_answer_set(self, facts, opt=True):
        """
        Args:
            facts (str): a string of ASP facts
            opt (bool): if true, only optimal answer sets are returned
                        leave it to False when there is no weak constraint
        """
        program = self.asp_program + facts
        clingo_control = Control(['0', '--warn=none', '--opt-mode=optN', '-t', '4'])
        models = []
        try:
            clingo_control.add('base', [], program)
            clingo_control.ground([('base', [])], context=Context())
        except:
            print(facts)
            breakpoint()
            return []
        if opt:
            clingo_control.solve(on_model = lambda model: models.append(model.symbols(atoms=True)) if model.optimality_proven else None)
        else:
            clingo_control.solve(on_model = lambda model: models.append(model.symbols(atoms=True)))
        models = [[str(atom) for atom in model] for model in models]
        return models
    
    def parse_answer_sets(self, answer_sets, bowls):
        plans, short_plans = [], ''
        for answer_set in answer_sets:
            # find the order list of actions
            actions = [atom.replace('pick_and_place(', '')[:-1] for atom in answer_set if atom.startswith('pick_and_place')]
            actions = [s.replace('\"','').split(',') for s in actions]
            actions.sort(key=lambda x: int(x[-1]))
            # find the states after each action
            plan, states_sentence = 'Plan:\n', [''] * len(actions)
            states = [atom.replace('on(', '')[:-1] for atom in answer_set if atom.startswith('on') and atom[-2].isdigit()]
            states = [s.replace('\"','').split(',') for s in states]
            states = [s for s in states if s[0].endswith('block')]
            states.sort(key=lambda x: (int(x[-1]), self.sort_order[x[0]]))
            for up, down, step in states:
                if step == '0':
                    continue
                states_sentence[int(step)-1] += f'The {up} is on the {down}.\n'
            for i, action in enumerate(actions):
                plan += f'{i+1}. Move the {action[0]} onto the {action[1]}.\n\n# State:\n'
                short_plans += f'{i+1}. Move the {action[0]} onto the {action[1]}.\n'
                plan += states_sentence[i]
                # add the description for empty bowl
                for bowl in bowls:
                    if bowl not in states_sentence[i]:
                        plan += f'Nothing is on the {bowl}.\n'
                plan += '\n'
            try:
                plan += f'{i+2}. Done'
            except:
                breakpoint()
                a = 0
            short_plans += '\n'
            plans.append((plan, len(actions)))
        return plans, short_plans.strip()

    def gen_data(self, n_data, min_stack, add_bowl, max_height, min_steps=1, max_trial=1000, seed=0):
        random.seed(seed)
        data, visited_states, stack_fact = [], set(), f'#const max_height={max_height}.\n'
        for _ in range(max_trial):
            if len(data) >= n_data:
                break
            """
            We randomly initialize n_stacks stacks and n_blocks blocks
            if add_bowl: min_stack <= n_stacks <= 7 and n_stacks <= n_blocks <= 7
            else: min_stack <= n_stacks <= max(3, min_stack+1) and n_stacks <= n_blocks <= 7
            """
            # randomly select the number of stacks and blocks
            if add_bowl:
                n_stacks = random.randint(min_stack, 7)
            else:
                # for pure block world domain, we limit the number of stacks
                n_stacks = random.randint(min_stack, max(3, min_stack+1))
            n_blocks = random.randint(n_stacks, min(7, n_stacks * max_height))
            # we assume that, for each stack there is a bowl (will be added later if add_bowl)
            # and for each bowl, there is always a block with the same color
            blocks = random.sample(self.rainbow_colors, n_blocks)
            bowls = random.sample(blocks, n_stacks)
            blocks = [color + ' block' for color in blocks]
            bowls = [color + ' bowl' for color in bowls]
            # randomly generate the init and goal state and its ASP form
            state, state_asp = {}, {}
            for type in ('init', 'goal'):
                count_blocks = [0] * n_stacks
                if add_bowl:
                    stacks = [[bowl] for bowl in bowls]
                else:
                    stacks = [[] for _ in bowls]
                for block in blocks:
                    # find which stacks still have room to add a block
                    available_indices = [i for i in range(n_stacks) if count_blocks[i] < max_height]
                    # randomly choose a stack and add the current block on it
                    index = random.choice(available_indices)
                    stacks[index].append(block)
                    count_blocks[index] += 1
                # if no bowl is added, we order the stacks by the first block
                if not add_bowl:
                    stacks = [stack for stack in stacks if stack]
                    stacks.sort(key=lambda x: self.sort_order[x[0]])
                state[type], state_asp[type] = self.interpret_state(stacks)

            # ignore this sample if the intial and goal states are the same
            if state['init'] == state['goal']:
                continue
            # ignore this sample if it's visited
            if state['init'] + '#' + state['goal'] in visited_states:
                continue

            # use ASP to find the plan
            answer_sets = self.gen_answer_set(
                stack_fact + state_asp['init'].replace(')', ', 0)') + state_asp['goal'])
            plans, short_plans = self.parse_answer_sets(answer_sets, bowls)
            if plans:
                plan, num_steps = plans[0]
            else:
                plan, num_steps = '', -1
            if num_steps >= min_steps:
                data.append((
                    state['init'], state['goal'], short_plans, plan,
                    n_stacks, n_blocks, num_steps,
                    state_asp['init'], state_asp['goal']
                    ))
            visited_states.add(state['init'] + '#' + state['goal'])
        df = pd.DataFrame(data, columns=self.column_names)
        df = df.sort_values(by='number of steps', ascending=True)
        df = df.reset_index(drop=True)
        # filename = f'numData={n_data}_minStack={min_stack}_bowl={add_bowl}_minSteps={min_steps}_maxHeight={max_height}_seed={seed}.xlsx'
        # df.to_excel(filename)
        filename = f'numData={n_data}_minStack={min_stack}_bowl={add_bowl}_minSteps={min_steps}_maxHeight={max_height}_seed={seed}.csv'
        df.to_csv(filename, sep='\t', encoding='utf-8')


def main(args):
    blockworld = BlockWorldData()
    blockworld.gen_data(args.n_data, args.min_stack, add_bowl=args.bowl,
        max_height=args.max_height, min_steps=args.min_steps, seed=args.seed)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--n_data', default=10, type=int,
        help='the number of data to be generated')
    parser.add_argument('--min_stack', default=3, type=int,
        help='the minimum number of stacks in each sample')
    parser.add_argument('--bowl', default=False, action='store_true',
        help='if true, add a bowl for each stack')
    parser.add_argument('--min_steps', default=3, type=int,
        help='the minimum number of steps required to solve each sample')
    parser.add_argument('--max_height', default=2, type=int,
        help='the maximum number of blocks stacked in a column')
    parser.add_argument('--seed', default=0, type=int,
        help='the random seed to generate the data instances')
    args = parser.parse_args()
    main(args)