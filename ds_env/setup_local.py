
# coding: utf-8

# # Table of Contents
#  <p><div class="lev1 toc-item"><a href="#How-to-setup-the-computer-for-data-science" data-toc-modified-id="How-to-setup-the-computer-for-data-science-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>How to setup the computer for data science</a></div><div class="lev2 toc-item"><a href="#Docker" data-toc-modified-id="Docker-11"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Docker</a></div><div class="lev2 toc-item"><a href="#Conda" data-toc-modified-id="Conda-12"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Conda</a></div><div class="lev2 toc-item"><a href="#Git" data-toc-modified-id="Git-13"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Git</a></div><div class="lev2 toc-item"><a href="#Setup-secrets" data-toc-modified-id="Setup-secrets-14"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>Setup secrets</a></div><div class="lev2 toc-item"><a href="#Setup-.bash_profile" data-toc-modified-id="Setup-.bash_profile-15"><span class="toc-item-num">1.5&nbsp;&nbsp;</span>Setup <code>.bash_profile</code></a></div><div class="lev2 toc-item"><a href="#R" data-toc-modified-id="R-16"><span class="toc-item-num">1.6&nbsp;&nbsp;</span>R</a></div><div class="lev2 toc-item"><a href="#Other-tools" data-toc-modified-id="Other-tools-17"><span class="toc-item-num">1.7&nbsp;&nbsp;</span>Other tools</a></div>

# # How to setup the computer for data science
# 
# This is a checklist of setup stuff for a new computer. 
# 
# ## Docker
# Install [docker](https://www.docker.com/) and setup [data science docker images](docker/setup_docker.md). Most setup stuff should be taken care of by this.
# 
# ## Conda
# It is still handy to have conda installed locally. Install conda 3. If want to have Python 2.7 available and with everything that comes with anaconda:
# ```sh
# conda create -n py27 python=2.7 anaconda
# ```
# 
# ## Git
# Create these aliases in `~/.gitconfig`
# ```sh
# [alias]
#   co = checkout
#   ci = commit
#   st = status
#   br = branch
#   hist = log --pretty=format:'%h %ad | %s%d [%an]' --graph --date=short
#   wdiff = diff --color-words
#   type = cat-file -t
#   dump = cat-file -p
# ```
# 
# ## Setup secrets
# Create the folder `/Users/yangzhang/Google\ Drive/secrets/` with `__init__.py` and `secrets.py` with something like:
# ```py
# AWS_KEY='ABC123'
# AWS_SECRET='ABCXYZ'
# 
# KAGGLE_USER='zhangyang'
# KAGGLE_PW='123'
# ```
# 
# ## Setup `.bash_profile`
# Add secrets to `PYTHONPATH`:
# ```sh
# export PYTHONPATH="/Users/yangzhang/git/secrets:$PYTHONPATH"
# 
# ```
# Create some handy shortcuts:
# ```sh
# alias jn='jupyter notebook'
# alias sa='source activate'
# alias sda='source deactivate'
# ```
# 
# ## R
# Two ways to install R:
# - Install R and RStudio.
# - Add R kernal to conda to make it available in Jupyter notebook:
# ```
# conda install -c r r-essentials
# ```
# 
# ## Other tools 
# - Pycharm
# - Sublime
# 
# [Home](https://yang-zhang.github.io/)
