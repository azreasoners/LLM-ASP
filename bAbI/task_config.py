

# =============================================================================
# data paths
# =============================================================================
data_paths={1:'qa1_single-supporting-fact_test.txt',
            2:'qa2_two-supporting-facts_test.txt',
            3:'qa3_three-supporting-facts_test.txt',
            4:'qa4_two-arg-relations_test.txt',
            5:'qa5_three-arg-relations_test.txt',
            6:'qa6_yes-no-questions_test.txt',
            7:'qa7_counting_test.txt',
            8:'qa8_lists-sets_test.txt',
            9:'qa9_simple-negation_test.txt',
            10:'qa10_indefinite-knowledge_test.txt',
            11:'qa11_basic-coreference_test.txt',
            12:'qa12_conjunction_test.txt',
            13:'qa13_compound-coreference_test.txt',
            14:'qa14_time-reasoning_test.txt',
            15:'qa15_basic-deduction_test.txt',
            16:'qa16_basic-induction_test.txt',
            17:'qa17_positional-reasoning_test.txt',
            18:'qa18_size-reasoning_test.txt',
            19:'qa19_path-finding_test.txt',
            20:'qa20_agents-motivations_test.txt'}

# =============================================================================
# default arguments
# iterative indicates that the context will be broken up into lines to be sent into GPT-3, otherwise it is sent in all at once.
# context_preprocess is a function that transforms the context before it is appended to the GPT-3 prompts, if no alterations are needed then None should be specified
# stop indicates the stop words that will be used in the GPT-3 call
# parse_word are any additional strings that will be appended to the end of the context
# sleep indicates the amount of times to wait before calling GPT-3 again. The default of 2 seconds should be fine. Increase this if the API returns a rate limit error
# modules are the ASP modules to be used for the task
# temporal stamp indicates whether to add a time stamp to facts returned by GPT-3
# separate indicates whether the context and query are parsed separately or with a single call
# answer fact specifices the relevant answer facts to extract
# custom parse specifies a function which contains GPT-3 calls for a task that may require custom prompting (i.e. chain of thought)
# post-processing specifies a function which may process the answer fact further so it can be cmopared to the ground truth
# =============================================================================
default_args = {'iterative':False, 
                'context_preprocess': None,
                'stop':None, 
                'parse_word': '\n', 
                'sleep':2, 
                'modules':[], 
                'temporal_stamp' : True, 
                'separate':True, 
                'answer_fact': {'predicate_name':'answer','relevant_terms_inds':[0], 'specified_terms' :{}}, 
                'custom_parse':False,
                'post_processing':lambda x,_ : x[0][0]}


class Config:
    ''' Configuration object which will store the task-specific information '''
    def __init__(self,args_dict):
        args_dict = {**default_args,**args_dict}
        for arg,item in args_dict.items():
            setattr(self,arg,item)


# Define and import any task-specific functions
direction_map = {'south':'s', 'north': 'n', 'east':'e', 'west':'w'}
def order_plan(facts,answer):
    
    facts.sort(key = lambda x: x[1])
    return ','.join([direction_map[fact[0]] for fact in facts])

from babi_utils import custom17

def post_process8(preds,answer):
    if len(preds)==1:
        return preds[0][0]
    elif len(preds)>=2:
        split_answer = answer.split(',')
        preds=[p[0] for p in preds]
        if preds==split_answer:
            preds = ','.join(preds)
        else:
            preds = ','.join(preds[::-1])
        return preds
    else:
        return 'nothing'

def post_process16(preds,answer):
    if len(preds)==1:
        return preds[0][0]
    else:
        for pred in preds:
            if pred[0]==answer:
                return pred[0]
    return ''
def preprocess4(context):
    return context.replace('\n','')


# Specify all task configurations and store in a dictionary 
task1_dict = {'iterative':True,'stops': 2*[None],'parse_word':2*['\nSemantic parse:'], 'modules':['DEC_AXIOMS','action']}
task2_dict = {'iterative':True,'stops': 2*[None],'parse_word':2*['\nSemantic parse:'], 'modules':['DEC_AXIOMS','action']}
task3_dict = {'iterative':True,'stops': 2*[None],'parse_word':2*['\nSemantic parse:'], 'modules':['DEC_AXIOMS','action']}
task4_dict = {'iterative':True,'context_preprocess' : preprocess4, 'stops': 2*[None],'parse_word':2*['\nSemantic parse:'], 'modules':['location'], 'temporal_stamp':False}
task5_dict = {'iterative':True,'stops': 2*[None],'parse_word':2*['\nSemantic parse:'], 'modules':['DEC_AXIOMS','action']}
task6_dict = {'iterative':True,'stops': 2*[None],'parse_word':2*['\nSemantic parse:'], 'modules':['DEC_AXIOMS','action']}
task7_dict = {'iterative':True,'stops': 2*[None],'parse_word':2*['\nSemantic parse:'], 'modules':['DEC_AXIOMS','action']}
task8_dict = {'iterative':True,'stops': 2*[None],'parse_word':2*['\nSemantic parse:'], 'modules':['DEC_AXIOMS','action'], 'post_processing':post_process8}
task9_dict = {'iterative':True,'stops': 2*[None],'parse_word':2*['\nSemantic parse:'], 'modules':['DEC_AXIOMS','action']}
task10_dict = {'iterative':True,'stops': 2*[None],'parse_word':2*['\nSemantic parse:'], 'modules':['DEC_AXIOMS','action'], 'temporal_stamp':True}
task11_dict = {'iterative':False,'stops': ['Sentences'],'parse_word':2*['\nSemantic parse:'], 'modules':['DEC_AXIOMS','action'], 'temporal_stamp':True, 'separate' : True}
task12_dict = {'iterative':True,'stops': 2*[None],'parse_word':2*['\nSemantic parse:'], 'modules':['DEC_AXIOMS','action']}
task13_dict = {'iterative':False,'stops': ['Sentences'],'parse_word':2*['\nSemantic parse:'], 'modules':['DEC_AXIOMS','action'], 'temporal_stamp':True, 'separate' : True}
task14_dict = {'iterative':True,'stops': 2*[None],'parse_word':2*['\nSemantic parse:'], 'modules':['DEC_AXIOMS','action'], 'temporal_stamp':False}
task15_dict = {'iterative':True,'stops': 2*[None],'parse_word':2*['\nSemantic parse:'], 'modules':[], 'temporal_stamp':False, 'separate' : True}
task16_dict = {'iterative':True,'stops': 2*[None],'parse_word':2*['\nSemantic parse:'], 'temporal_stamp':False, 'post_processing':post_process16, 'separate':True}#'answer_fact': {'predicate_name':'isColor','relevant_terms_inds':[1], 'specified_terms' :{0:'action',1:'agent'}}}
task17_dict = {'iterative':False,'stops': ['Sentences', 'Objects'],'parse_word':['\nObjects:', '\nQuery Fact: '], 'modules':['location'], 'temporal_stamp':False, 'separate':True, 'custom_parse':custom17}
task18_dict = {'iterative':True,'stops': 2*[None],'parse_word':2*['\nSemantic parse:'], 'modules':[], 'temporal_stamp':False}
task19_dict = {'iterative':True,'stops': 2*[None],'parse_word':2*['\nSemantic parse:'], 'modules':['DEC_AXIOMS','action', 'location'], 'temporal_stamp':False, 'separate':True, 'post_processing':order_plan, 'answer_fact': {'predicate_name':'happens','relevant_terms_inds':[3,4], 'specified_terms' :{0:'action',1:'agent'}}}
task20_dict = {'iterative':True,'stops': 2*[None],'parse_word':2*['\nSemantic parse:'], 'temporal_stamp':False, 'separate':True}


tasks_dict = {1: task1_dict,
              2: task2_dict,
              3: task3_dict,
              4: task4_dict,
              5: task5_dict,
              6: task6_dict,
              7: task7_dict,
              8: task8_dict,
              9: task9_dict,
              10: task10_dict,
              11: task11_dict,
              12: task12_dict,
              13: task13_dict,
              14: task14_dict,
              15: task15_dict,
              16: task16_dict,
              17: task17_dict,
              18: task18_dict,
              19: task19_dict,
              20: task20_dict}

