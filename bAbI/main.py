import os
import openai
import argparse
from tqdm import tqdm
import pickle
import sys
sys.path.append('../')

from GPT_prompts import prompts
from asp_domains import babi_tasks
from asp_modules import *

from keys import API_KEY,ORG_KEY

from task_config import tasks_dict, data_paths, Config
from babi_utils import get_query, GPT_parse, ASP_solve, process_answer_set, write_debug

parser = argparse.ArgumentParser()

parser.add_argument('--n', default = 100, type = int, help = 'Specifies the number of examples to run.')
parser.add_argument('--task', default = 1, type = int, help = 'Specifies task number (1-20).')
parser.add_argument('--ALL', action = 'store_true', help = 'Specifies all 20 tasks.')
parser.add_argument('--model', default = 'text-davinci-003', type = str, help = 'Specifies model (supports "text-davinci-002" and "text-davinci-003")')


args=parser.parse_args()


gpt_model = args.model 

# Assign openai API key
openai.organization = ORG_KEY
openai.api_key = API_KEY

task_nums = [args.task]
if args.ALL:
    task_nums = [i+1 for i in range(0,20)]
else:
    task_nums = [args.task]

# Load previous GPT-3 responses
if f'prompt_cache_{gpt_model}.pickle' in os.listdir():
    with open(f'prompt_cache_{gpt_model}.pickle', 'rb') as handle:
        prompt_cache = pickle.load(handle)
else:
    prompt_cache = dict()

for task_idx in task_nums:
    
    # Read Data
    data_path = os.path.join('data',data_paths[task_idx])
    with open(data_path) as f:
        lines = f.readlines()
    beginning_lines=[idx for idx,line in enumerate(lines) if int(line[:2])==1]
    question_lines = [idx for idx,line in enumerate(lines) if '?' in line]
    
    # Load task configuration object
    config=Config(tasks_dict[task_idx])
    
    print(f"Evaluating task {task_idx}")
    task_rules = babi_tasks[task_idx]
    # Load task-relevant modules 
    module_rules = '\n\n'.join([asp_modules_dict[module] for module in config.modules])
    print(f"Using modules {config.modules}")
    task_prompts=prompts[task_idx]
    
    # Main Evaluation Loop
    stop = config.stop
    parse_word = config.parse_word
    correct,total=0,0
    wrong_indices=list()
    pbar= tqdm(range(0, args.n))
    accuracies,debug=list(), list()
    for eval_num in pbar:
        # 1. Process data instance and prepare data for GPT-3
        context, query, answer  = get_query(eval_num,lines, beginning_lines , question_lines)
        # 2. Call GPT-3
        instance_string, prompt_cache = GPT_parse(task_prompts, context, query, gpt_model, config, prompt_cache)
        # 3. Concatenate GPT-3 generated facts with task rules and relevant module rules 
        ASP_program = instance_string + task_rules + module_rules
        # 4. Run ASP program
        try:
            answer_set = ASP_solve(ASP_program)
            # 5. Get prediction from answer set
            pred = process_answer_set(answer_set, config.answer_fact, config.post_processing, answer)
        except:
            pred=''
        if pred==answer.lower():
            correct+=1
        else:
            wrong_indices.append(eval_num)
            debug.append([eval_num, context, query, instance_string, ASP_program, pred, answer])
        total+=1
        accuracies.append(correct/total)
        pbar.set_description(f'acc: {100*correct / total}')
    #write_debug(debug, correct, total, task_idx, 'test')
    # Save GPT-3 responses
    with open(f'prompt_cache_{gpt_model}.pickle', 'wb') as handle:
        pickle.dump(prompt_cache, handle, protocol=pickle.HIGHEST_PROTOCOL)
