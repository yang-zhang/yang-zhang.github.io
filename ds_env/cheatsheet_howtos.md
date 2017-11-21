# Cheatsheet: howtos

## Git

### Enable credentials storage 
```sh
git config credential.helper store
```

### Add upstream repository
```sh
git remote add upstream https://github.com/scikit-learn/scikit-learn.git
```

### Check out remote branch
```sh
git fetch origin
git checkout --track -b some_branch origin/somebrach
```

### Git setup for contributing to repo
- Fork the repo on github (e.g. https://github.com/dmlc/xgboost)
- Clone your forked repo: git clone https://github.com/yang-zhang/xgboost
- Add original owner’s repository: cd xgboost; git remote add dmlc https://github.com/dmlc/xgboost
- Show remote repo: git remote -v
See [here](http://kbroman.org/github_tutorial/pages/fork.html) for reference.

### Add remote branch
```
git checkout -b name_of_branch origin/name_of_branch

git fetch upstream
git checkout --track upstream/name_of_branch
```

## Keras
Switch backend temporarily:
In shell:
```sh
KERAS_BACKEND=tensorflow ipython
```
or in notebook:
```sh
%env KERAS_BACKEND=tensorflow
```

## Docker
### Get image and run
```
docker pull julia
docker run -it --rm julia
```

### Get inside a running container
```
docker ps
sudo docker exec -it gallant_fermat bash
```

### Get inside the most recent running container
```
docker exec -it $(docker ps -l -q) bash
```

### Stop and delete all containers
```
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
```

### Build image
```
docker build --file dockerfiles/yang-zhang-ds.docker -t yang-zhang-ds .
```

### Map disk and run
```
docker run -it --rm -v "$PWD":/usr/myapp -w /usr/myapp julia julia test.jl
```

### Append to env variables
```
docker run --rm -v $PWD:/tmp -it yang-zhang-ds bash -c 'export PYTHONPATH=$PYTHONPATH:/tmp/ds-utils; bash' 
```



## Misc Hacks

### Clone from existing env in conda
```
conda create -n new_env --clone root
```

### Imports
Use a [customerized import script](https://github.com/yang-zhang/ds-utils/blob/master/ds_utils/imports.py) for frequent modules and setups. Add the following to the beginning of code:
```
import ds_utils.imports; import imp; imp.reload(ds_utils.imports)
from ds_utils.imports import
```

### xgboost
Conda's version is old.
```
cd Downloads
git clone --recursive https://github.com/dmlc/xgboost
cd xgboost; cp make/minimum.mk ./config.mk; make -j4
cd python-package; sudo python setup.py install
```

Add [ds-utils](https://github.com/yang-zhang/ds-utils) to path:


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

### Kaggle
```
!kg config -g -u $KAGGLE_USER -p $KAGGLE_PW -c $competition_name
!kg download
!kg submit $submit_file -u $KAGGLE_USER -p $KAGGLE_PW -m $model_description
```

### Install R packages in Jupyter notebook 

### In code
```
from rpy2.robjects.packages import importr
utils = importr('utils')
utils.install_packages(ro.StrVector(['entropy', 'psych', 'vcd']))
```

### Run a R kernal in Jupyter and run
install.packages(c('entropy', 'psych', 'vcd'))

[Home](https://yang-zhang.github.io/)
