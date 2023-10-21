# GPT3-R
This is the repository for the paper [Coupling Large Language Models with Logic Programming for Robust and General Reasoning from Text](https://aclanthology.org/2023.findings-acl.321.pdf) in Findings of ACL 2023.
[Lab Page](https://azreasoners.github.io/ARG-webpage/)
## Installation
```
conda create --name gpt3-r -c conda-forge python=3.11
conda activate gpt3-r
conda install -c conda-forge openai clingo=5.6 tqdm
```

## How to run
Please update line 11 of file `pipeline.py` with your OpenAI API key. Then, to run the experiments for each dataset, simply follow the instructions in the README file in the respective data folder.

## Citation
Please cite our paper as:
```
@inproceedings{yang-etal-2023-coupling,
    title = "Coupling Large Language Models with Logic Programming for Robust and General Reasoning from Text",
    author = "Yang, Zhun  and
      Ishay, Adam  and
      Lee, Joohyung",
    booktitle = "Findings of the Association for Computational Linguistics: ACL 2023",
    month = jul,
    year = "2023",
    address = "Toronto, Canada",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2023.findings-acl.321",
    doi = "10.18653/v1/2023.findings-acl.321",
    pages = "5186--5219"
}
```
