# Software Setup
Setting up software environement for Data Science.

## Conda
Environment
If you have conda3, Install Python2.7 with everything that comes with anaconda
```
conda create -n py27 python=2.7 anaconda
```
If you have conda2, Install Python3.5 with everything that comes with anaconda
```
conda create -n py35 python=3.5 anaconda
```
Clone from existing env
```
conda create -n new_env --clone root
```

## Setup `.bash_profile`
Add [ds-utils](https://github.com/yang-zhang/ds-utils) to path:
```
export PYTHONPATH="/Users/yangzhang/git/ds-utils:/Users/yangzhang/git/secrets:$PYTHONPATH"

alias jn='jupyter notebook'
alias sa='source activate'
alias sda='source deactivate'
```

## Setup `secrets.py`
In `~/git/secrets/secrets.py`, add:
```
AWS_KEY='ABC123'
AWS_SECRET='ABCXYZ'

KAGGLE_USER='zhangyang'
KAGGLE_PW='123'
```

## Imports
Use a [customerized import script](https://github.com/yang-zhang/ds-utils/blob/master/ds_utils/imports.py) for frequent modules and setups. Add the following to the beginning of code:
```
import ds_utils.imports; import imp; imp.reload(ds_utils.imports)
from ds_utils.imports import
```

## xgboost
Conda's version is old.
```
cd Downloads
git clone --recursive https://github.com/dmlc/xgboost
cd xgboost; cp make/minimum.mk ./config.mk; make -j4
cd python-package; sudo python setup.py install
```

## R

### Add R kernal:
```
conda install -c r r-essentials
```
### Install package

#### In code
```
from rpy2.robjects.packages import importr
utils = importr('utils')
utils.install_packages(ro.StrVector(['entropy', 'psych', 'vcd']))
```

#### Run a R kernal in Jupyter and run
install.packages(c('entropy', 'psych', 'vcd'))

## Git
### Aliases in `~/.gitconfig`
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
### Git setup for contributing to repo
- Fork the repo on github (e.g. https://github.com/dmlc/xgboost)
- Clone your forked repo: git clone https://github.com/yang-zhang/xgboost
- Add original owner’s repository: cd xgboost; git remote add dmlc https://github.com/dmlc/xgboost
- Show remote repo: git remote -v
See [here](http://kbroman.org/github_tutorial/pages/fork.html) for reference.

### Add remote branch
```
git checkout --track origin/name_of_the_remote_branch
```

## Misc Hacks

### Python 2 to 3
```
2to3 -w example.py
```

### Control video speed
- [Google YouTube Keyboard Shortcuts](https://sites.google.com/a/umich.edu/going-google/accessibility/google-keyboard-shortcuts---youtube)
- [Video Speed Controller - Chrome extension](https://chrome.google.com/webstore/detail/video-speed-controller/nffaoalbilbmmfgbnbgppjihopabppdk)

### Kaggle
```
!kg config -g -u $KAGGLE_USER -p $KAGGLE_PW -c $competition_name
!kg download
!kg submit $submit_file -u $KAGGLE_USER -p $KAGGLE_PW -m $model_description
```
### Make `top` sort by memory usage
```
top -o MEM
```
### [Add link to imported modules on github](http://fiatjaf.alhur.es/module-linker/#/python)
### [Move tabs using keyboard in Chrome](https://chrome.google.com/webstore/detail/moigagbiaanpboaflikhdhgdfiifdodd)
### [Glenn Gould](https://music.amazon.com/artists/B000QKLXBO/CATALOG?ref=dm_wcp_artist_link_pr_s)
