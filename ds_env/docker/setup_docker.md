## How to setup docker for data science
Most setup stuff should be taken care of by this.

### Step-1: find a good base docker image as a starting point.
For example, [kaggle/python](https://github.com/Kaggle/docker-python).

### Step-2: make changes to the docker image as needed.
Install additional packages and copy additional files, for [example](https://github.com/yang-zhang/yang-zhang.github.io/blob/master/ds_env/docker/dockerfiles/yang-zhang-ds.docker):
```dockerfile
FROM kaggle/python:latest

RUN conda install -c conda-forge jupyter_contrib_nbextensions && \
    conda install -c conda-forge jupyter_nbextensions_configurator && \
    conda install -c conda-forge yapf=0.13.2 && \
    conda install -c r rpy2=2.8.5 && \
    conda install pytorch torchvision -c soumith && \
    conda install -c conda-forge feather-format=0.3.1 && \
    pip install graphviz && \
    pip install pydot-ng && \
    pip install kaggle-cli && \
    pip install mxnet && \
    # Enable favorite jupyter notebook extensions (https://github.com/ipython-contrib/jupyter_contrib_nbextensions#3-enablingdisabling-extensions)
    jupyter nbextension enable toc2/main && \
    jupyter nbextension enable code_prettify/code_prettify
ADD jupyter_notebook_config.py /root/.jupyter/
```

### Step-3: build the docker image.
Under [ds_env](https://github.com/yang-zhang/yang-zhang.github.io/tree/master/ds_env), run
```sh
docker build --file docker/dockerfiles/yang-zhang-ds.docker -t yang-zhang-ds .
```

### Step-4: run the docker image.
In `.bash_profile`, add shortcuts to the command to run python, ipython, jupyter notebook, and bash in the docker image:
```sh
# For docker begin
alias dcf='declare -F'

# run jupyter notebook in docker
jn_dk() {
    docker run \
    -v ~/git:/tmp \
    -v ~/Google\ Drive/secrets:/tmp/secrets \
    -v ~/Google\ Drive/git:/tmp/git_2 \
    -v ~/Storage:/tmp/storage \
    -w=/tmp \
    -p 8888:8888 \
    --rm -it yang-zhang-ds \
    bash -c 'export PYTHONPATH=$PYTHONPATH:/tmp/ds-utils:/tmp/secrets; jupyter notebook --no-browser --allow-root --ip="0.0.0.0" --notebook-dir=/tmp'
}

# run python in docker
python_dk() {
    docker run \
    -v ~/git:/tmp -w=/tmp\
    --rm -it yang-zhang-ds \
    bash -c 'export PYTHONPATH=$PYTHONPATH:/tmp/ds-utils:/tmp/secrets; python "$@"'
}
# run ipython in docker
ipython_dk() {
    docker run \
    -v ~/git:/tmp -w=/tmp \
    --rm -it yang-zhang-ds \
    bash -c 'export PYTHONPATH=$PYTHONPATH:/tmp/ds-utils:/tmp/secrets; ipython'
}
# run bash in docker
dk_ds() {
    docker run \
    -v ~/git:/tmp -w=/tmp \
    --rm -it yang-zhang-ds \
    bash -c 'export PYTHONPATH=$PYTHONPATH:/tmp/ds-utils:/tmp/secrets; bash'
}

# For docker end
```
Note that the `$PYTHONPATH` is updated in the container to include the local packages you want to add. In this example, jupyter notebook is running on `0.0.0.0:8888`.

[Home](https://yang-zhang.github.io/)
