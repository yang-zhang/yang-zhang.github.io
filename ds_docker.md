# Simple steps to using docker for data science

### Step-1: find a good docker image
For example, [kaggle/python](https://github.com/Kaggle/docker-python).

### Step-2: make changes to the docker image
Install additional packages and copy additional files, for [example](https://github.com/yang-zhang/ds-env/blob/master/docker/dockerfiles/yang-zhang-ds.docker):
```dockerfile
FROM kaggle/python:latest

RUN conda install -c conda-forge jupyter_contrib_nbextensions && \
    conda install -c conda-forge jupyter_nbextensions_configurator && \
    conda install -c conda-forge yapf=0.13.2 && \
    conda install -c r rpy2=2.8.5 && \
    pip install kaggle-cli
ADD jupyter_notebook_config.py /root/.jupyter/
```

### Step-3: build the docker image 
For [example](https://github.com/yang-zhang/ds-env/blob/master/setup_docker.md):
```
docker build --file docker/dockerfiles/yang-zhang-ds.docker -t yang-zhang-ds .
```

### Step-4: run docker image 
In `.bash_profile`, add shortcuts to the command to run python, ipython, jupyter notebook, and bash in the docker image. For [example](https://github.com/yang-zhang/ds-env/blob/master/setup_docker.md):
```bash
# run python in docker
python_dk() {
  docker run -v ~/git:/tmp -w=/tmp  --rm -it yang-zhang-ds bash -c 'export PYTHONPATH=$PYTHONPATH:/tmp/ds-utils:/tmp/secrets; python "$@"'
}
# run ipython in docker
ipython_dk() {
  docker run -v ~/git:/tmp -w=/tmp --rm  -it yang-zhang-ds bash -c 'export PYTHONPATH=$PYTHONPATH:/tmp/ds-utils:/tmp/secrets; ipython'
}
# run jupyter notebook in docker
jn_dk() {
  docker run -v ~/git:/tmp -w=/tmp -p 8888:8888 --rm -it yang-zhang-ds bash -c 'export PYTHONPATH=$PYTHONPATH:/tmp/ds-utils:/tmp/secrets; jupyter notebook --no-browser --ip="0.0.0.0" --notebook-dir=/tmp' 
}
# run bash in docker
dk_ds() {
  docker run --rm -v ~/git:/tmp -it yang-zhang-ds bash -c 'export PYTHONPATH=$PYTHONPATH:/tmp/ds-utils:/tmp/secrets; bash'
}
```
Note that the `$PYTHONPATH` is updated in the container to include the local packages you want to add. In this example, jupyter notebook is running on `0.0.0.0:8888`.

---
[View Source](https://github.com/yang-zhang/yang-zhang.github.io)
[GitHub Repositories](https://github.com/yang-zhang)
