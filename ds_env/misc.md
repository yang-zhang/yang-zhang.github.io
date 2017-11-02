# Misc tips and tricks

### Save git credential to avoid typing user and pw repeatedly
```sh
git config --global credential.helper cache
```

### Download file from jupyter notebook
```py
from IPython.display import FileLink
FileLink('something.csv')
```

### Conda Clone from existing env
```
conda create -n new_env --clone root
```

### xgboost
Conda's version is old.
```
cd Downloads
git clone --recursive https://github.com/dmlc/xgboost
cd xgboost; cp make/minimum.mk ./config.mk; make -j4
cd python-package; sudo python setup.py install
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


### Python 2 to 3
```
2to3 -w example.py
```

### Control video speed
- [Google YouTube Keyboard Shortcuts](https://sites.google.com/a/umich.edu/going-google/accessibility/google-keyboard-shortcuts---youtube)
- [Video Speed Controller - Chrome extension](https://chrome.google.com/webstore/detail/video-speed-controller/nffaoalbilbmmfgbnbgppjihopabppdk)

### Make `top` sort by memory usage
```
top -o MEM
```
### [Add link to imported modules on github](http://fiatjaf.alhur.es/module-linker/#/python)
### [Move tabs using keyboard in Chrome](https://chrome.google.com/webstore/detail/moigagbiaanpboaflikhdhgdfiifdodd)
### [Glenn Gould](https://music.amazon.com/artists/B000QKLXBO/CATALOG?ref=dm_wcp_artist_link_pr_s)

### Kaggle
```
!kg config -g -u $KAGGLE_USER -p $KAGGLE_PW -c $competition_name
!kg download
!kg submit $submit_file -u $KAGGLE_USER -p $KAGGLE_PW -m $model_description
```

### Install R package for in conda

#### In code
```
from rpy2.robjects.packages import importr
utils = importr('utils')
utils.install_packages(ro.StrVector(['entropy', 'psych', 'vcd']))
```

#### Run a R kernal in Jupyter and run
install.packages(c('entropy', 'psych', 'vcd'))

[Home](https://yang-zhang.github.io/)
