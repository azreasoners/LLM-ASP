## How to run
One can use the following command
```
python main.py --dataset [DATASET] --engine [ENGINE]
```
to evaluate our method on a clutrr dataset using a specific engine.

- `[DATASET]` could be `clutrr` (the original CLUTRR dataset), `clutrr_1.3` (our generated CLUTRR dataset with less errors using [CLUTRR 1.3 codes](https://github.com/facebookresearch/clutrr/tree/develop)), its cleaned version `clutrr_1.3_clean`, or `clutrr_s` (the simpler version of CLUTRR dataset from [DeepProbLog repository](https://github.com/ML-KULeuven/deepproblog/tree/master/src/deepproblog/examples/CLUTRR/data)). 

- `[ENGINE]` could be `text-davinci-003`, `text-davinci-002`, or `text-curie-001`.

- Please ignore the error messages, e.g.,
```
<block>:108:82-99: error: unsafe variables in:
  baby("Alice",#Anon0):-[#inc_base].
<block>:108:96-97: note: '#Anon0' is unsafe
```
printed out by the ASP solver [clingo](https://github.com/potassco/clingo) due to the invalid syntax of atoms in the GPT-3 responses. Note that a simple cleaning process as in stepGame doesn't improve the accuracy here as there are many different syntax errors that should be addressed.

- Example commands and results are available in `logs.txt` in this folder.

- This command will also generate a file `mistakes.xlsx` in the current folder, where each row denotes 1 wrong prediction. All GPT-3 responses that lead to clingo error messages can also be found in this file.
