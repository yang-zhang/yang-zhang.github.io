## How to setup the computer for data science

### Docker
Setup [docker](https://www.docker.com/) and [data science docker images](docker/setup_docker.md).


### Conda
Install conda (2 or 3). If want the other version of python available, e.g., if you have conda3 and want to have Python 2.7 available and with everything that comes with anaconda:
```
conda create -n py27 python=2.7 anaconda
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
```sh
export PYTHONPATH="/Users/yangzhang/git/secrets:$PYTHONPATH"

```

```
alias jn='jupyter notebook'
alias sa='source activate'
alias sda='source deactivate'
```

### R

#### Add R kernal to conda:
```
conda install -c r r-essentials
```
#### Install package

##### In code
```
from rpy2.robjects.packages import importr
utils = importr('utils')
utils.install_packages(ro.StrVector(['entropy', 'psych', 'vcd']))
```

##### Run a R kernal in Jupyter and run
install.packages(c('entropy', 'psych', 'vcd'))

### Git
#### Aliases in `~/.gitconfig`
``` 
[alias]
  co = checkout
  ci = commit
  st = status
  br = branch
  hist = log --pretty=format:'%h %ad | %s%d [%an]' --graph --date=short
  type = cat-file -t
  dump = cat-file -p
```

[Home](https://yang-zhang.github.io/)
