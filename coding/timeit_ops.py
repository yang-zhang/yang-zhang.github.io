
# coding: utf-8

# # Time cost of key operations in Python

# ## Creating `range(n)` is $O(1)$

# In[93]:

get_ipython().magic('timeit lst = range(10)')


# In[94]:

get_ipython().magic('timeit lst = range(10000000)')


# ## Retrieving any item by index in a list of length $n$ is $O(1)$

# In[100]:

lst = range(10)
get_ipython().magic('timeit lst[5]')


# In[101]:

lst = range(1000000)
get_ipython().magic('timeit lst[500000]')


# ## Converting a list of length $n$ to a set is $O(n)$

# In[102]:

lst = range(10)
get_ipython().magic('timeit st = set(lst)')


# In[103]:

lst = range(100000)
get_ipython().magic('timeit st = set(lst)')


# ## Checking membership in a set of size $n$ is $O(1)$

# In[108]:

st = set(range(10))
get_ipython().magic('timeit (-1 in st)')


# In[109]:

st = set(range(100000))
get_ipython().magic('timeit (-1 in st)')


# ## Converting a list of length $n$ to a dict is $O(n)$

# In[110]:

lst = range(10)
get_ipython().magic('timeit dct = {i:1 for i in lst}')


# In[111]:

lst = range(100000)
get_ipython().magic('timeit dct = {i:1 for i in lst}')


# ## Checking membership in a dict of size $n$ is $O(1)$

# In[112]:

dct = {i:1 for i in range(10)}
get_ipython().magic('timeit (-1 in dct)')


# In[113]:

dct = {i:1 for i in range(100000)}
get_ipython().magic('timeit (-1 in dct)')


# Reference:
# - High Performance Python
