## Why save a jupyter notebook as a python file?
Because notebooks are hard to version control - try `git diff [YOUR_NOTEBOOK].ipynb` after a few changes and see the mess. 

## How to save a juypter notebook as a python file?
1. Most obvious way is to manually download from the notebook: `File -> Download as -> Python (.py)`, find the python file from the Downloads folder, and copy to your repository.
2. A slightly better way is to run from the command line:
```
$ jupyter nbconvert --to script [NOTEBOOK_NAME].ipynb
``` 
or run the schell command in jupyter notebook:
```
!jupyter nbconvert --to script [NOTEBOOK_NAME].ipynb
```

## How to automatically save a jupyter notebook as a python file?
Follow this [post](http://protips.maxmasnick.com/ipython-notebooks-automatically-export-py-and-html) and save [this python file](https://github.com/yang-zhang/ds-env/blob/master/jupyter_notebook_config.py) (`jupyter_notebook_config.py`) as `~/.jupyter/jupyter_notebook_config.py`. 

## How to automatically save a jupyter notebook as a python file when you're running the notebook in a docker container?
Add `jupyter_notebook_config.py` to the a note to the `.jupyter` folder using the `ADD jupyter_notebook_config.py [HOME]/.jupyter/` command in the docerfile. See [here](https://github.com/yang-zhang/ds-env/blob/master/docker/dockerfiles/yang-zhang-ds.docker#L8) for a real example. For more details on using docker to run jupyter notebook and to do data science in general, see this [post](ds_docker.md).

## References:
- http://stackoverflow.com/questions/17077494/how-do-i-convert-a-ipython-notebook-into-a-python-file-via-commandline
- http://protips.maxmasnick.com/ipython-notebooks-automatically-export-py-and-html
