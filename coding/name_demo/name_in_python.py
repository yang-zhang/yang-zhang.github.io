
# coding: utf-8

# # What is the value of `__name__` in Python?
# 
# `__name__` is `__main` when run as a script; `__name__` is name of the module when imported as a module.
# Let's demo this using the script `name_demo.py`:

# In[7]:

cat name_demo.py


# `__name__` is `__main` when run as a script:

# In[8]:

get_ipython().system('python name_demo.py')


# `__name__` is name of the module (`name_demo`) when imported as a module:

# In[9]:

import name_demo


# In[10]:

name_demo.say_name()


# `import ... as ...` does not change `__name__`:

# In[11]:

import name_demo as nd


# In[12]:

name_demo.say_name()


# [Home](https://yang-zhang.github.io/)
