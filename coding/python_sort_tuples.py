
# coding: utf-8

# # How does Python sort tuples

# Python first compares items of the tuples in at `[0]`, then at `[1]`, `[2]`, ... , and so on.

# In[12]:

list_of_tuples = [(3, 2), (1, 2), (1, 5), (0, 3), (0, 3, 3), (0, 3, 1, 5)]


# In[13]:

list_of_tuples.sort()


# In[14]:

list_of_tuples

