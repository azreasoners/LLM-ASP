## [Optional] Data Generation
Go to the data folder with `cd data` and use the following commands to generate 20 data instances under different settings. 
- Generate 20 data instances with blocks only. Here, `min_stack` is the minimum number of stacks in both initial and goal states. `max_height` is the maximum number of blocks that can be stacked together.
```
python data_gen.py --n_data 20 --min_stack 1 --max_height 7
```
- Generate 20 data instances with blocks and bowls. Here, `--bowl` means bowls are added and the number of stacks equals to the number of bowls with one bowl at the bottom of each stack.
```
python data_gen.py --bowl --n_data 20 --min_stack 3 --max_height 2
```

## How to run
Go to the folder of this README file `cd pickPlace` and execute the following command. The options added below are default settings and one can apply a different GPT-3 engine to different number of test data. (Please refer to `main.py` for more details.)
```
python main.py --engine text-davinci-003 --num -1
```
Here, `--num -1` means to evaluate all test data in the test data files. One can also test the baseline with
```
python baseline.py --engine text-davinci-003 --num -1
```