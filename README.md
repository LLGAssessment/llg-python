# llg-python
A last letter game benchmark implemented in Python

## How to run
Clone repository recursively:

```bash
git clone --recursive https://github.com/LLGAssessment/llg-python.git
```

Run test and measure its time:

```bash
cd llg-python
time python llg.py < llg-dataset/70pokemons.txt
```

Of course you can use `pypy` for this benchmark:

```bash
time pypy llg.py < llg-dataset/70pokemons.txt
```
