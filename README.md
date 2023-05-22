# GPT3-R
This is the repository for the paper "Dual System Model: Coupling Large Language Models with Logic Programming for Robust and General Reasoning from Text".

## Installation
```
conda create --name gpt3-r -c conda-forge python=3.11
conda activate gpt3-r
conda install -c conda-forge openai clingo=5.6 tqdm
```

## How to run
Please update line 11 of file `pipeline.py` with your OpenAI API key. Then, to run the experiments for each dataset, simply follow the instructions in the README file in the respective data folder.
