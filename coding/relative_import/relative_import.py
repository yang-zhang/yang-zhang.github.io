
# coding: utf-8

# # Relative import in Python

# In[16]:

ls


# In[17]:

get_ipython().system('find some_folder/my_package/')


# In[3]:

import sys
import os
cwd = os.getcwd()
sys.path.append(cwd + '/some_folder')


# In[4]:

cat some_folder/my_package/module_1.py


# In[5]:

cat some_folder/my_package/package_1/module_2.py


# In[6]:

cat some_folder/my_package/package_1/module_3.py


# In[14]:

cat some_folder/my_package/package_1/package_2/module_4.py


# In[7]:

cat some_folder/my_package/package_1/package_2/module_5.py


# In[8]:

import my_package.package_1.package_2.module_5


# References: 
# - Pro Python

# [Home](https://yang-zhang.github.io/)
