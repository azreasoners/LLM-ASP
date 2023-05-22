## Preparation
Included is `prompt_cache_<method>_<GPT-model>.pickle` which includes outputs from GPT-3 for 1000 bAbI task test set queries. <!---This is automatically loaded in and means that you can run up the whole test set without requiring use of GPT-3. ---> If you delete this file or want to re-run the experiments from scratch, then GPT-3 use is required and a valid organization and API key should be filled in the `keys.py` file:

```
openai.organization = "ORG"
openai.api_key = "API-KEY"
```
## Run
To run the code, use one of the commands:

`python main.py` (for baseline)

`python main_cot.py` (for chain-of-thought)

By default 100 examples of task #1 are run. Arguments:  
`--n <number of examples to run` - specifies number of examples to run.  
`--task <task number>` - specifies the task number to run (integer).
`--ALL` - specifies to run all tasks.

For example: `python main.py --task 7 --n 10 `.
