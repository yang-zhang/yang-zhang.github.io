## How to setup the computer for data science

This is a checklist of setup stuff for a new computer. 

### Docker
Install [docker](https://www.docker.com/) and setup [data science docker images](docker/setup_docker.md). Most setup stuff should be taken care of by this.

### Conda
It is still handy to have conda installed locally. Install conda 3. If want to have Python 2.7 available and with everything that comes with anaconda:
```sh
conda create -n py27 python=2.7 anaconda
```

### Git
Create these aliases in `~/.gitconfig`
```sh
[alias]
  co = checkout
  ci = commit
  st = status
  br = branch
  hist = log --pretty=format:'%h %ad | %s%d [%an]' --graph --date=short
  type = cat-file -t
  dump = cat-file -p
```

### Setup `secrets.py`
In `/Users/yangzhang/Google\ Drive/secrets/secrets.py`, add:
```py
AWS_KEY='ABC123'
AWS_SECRET='ABCXYZ'

KAGGLE_USER='zhangyang'
KAGGLE_PW='123'
```

### Setup `.bash_profile`
Add secrets to `PYTHONPATH`:
```sh
export PYTHONPATH="/Users/yangzhang/git/secrets:$PYTHONPATH"

```
Create some handy shortcuts:
```sh
alias jn='jupyter notebook'
alias sa='source activate'
alias sda='source deactivate'
```

### R
Two ways to install R:
- Install R and RStudio.
- Add R kernal to conda to make it available in Jupyter notebook:
```
conda install -c r r-essentials
```

### Other tools 
- Pycharm
- Sublime

[Home](https://yang-zhang.github.io/)
