## Data Preparation
We use the StepGame dataset (with noise) under bAbI format from [StepGame](https://github.com/ZhengxiangShi/StepGame) repository. Please download all files from [this github folder](https://github.com/ZhengxiangShi/StepGame/tree/main/Code/babi_format/noise) and put them under the `stepGame/data/noise/` folder. (An example file `qa1_test.txt` is already put in this folder.)

## How to run the GPT-3 baselines
The following command will evaluate two GPT-3 baselines on the first 100 data instances for each k in 1, ..., 10.
```
python baseline.py --num 100 --engine text-davinci-003
```

## How to run with our method
To run the pipeline using "text-davinci-002" model, one can simply use the following command. This command will also generate a file `mistakes.xlsx` in the current folder, where each row denotes 1 wrong prediction. 
```
python main.py --num 1000 --engine text-davinci-002
```
One can also use the folloiwng command to use the "text-curie-001" model.
```
python main.py --num 1000 --engine text-curie-001
```
The logs of all experiments are available in `logs.txt` in this folder.

## Mistake Analyses
The `mistake_analyses/StepGame` folder (in the root folder) contains 10 excel files, one for each k in 1, ..., 10. Each file records the mistakes made on the first 100 data instances in a test datafile using the "text-davinci-002" model. One can reproduce these 10 excel files using the following command for 10 times, each time commenting out 9/10 files in `path_test_data_files` in `main.py`.
```
python main.py --num 100
```

## How to debug a wrong prediction
Open the generated file `mistakes.xlsx`, choose a cell under column `response`, save the content into `example.txt`, then use the following command to locate related sentences to the query.
```
clingo debug_sp.txt example.txt
```