
# coding: utf-8

# # Method Resolution Order (MRO) in Python

# In[7]:

class A:
    def __init__(self):
        self.some_attribute = "A"

class B:
    def __init__(self):
        self.some_attribute = "B"
        
class AB(A, B):
    pass

class BA(B, A):
    pass

ab = AB()
ba = BA()


# In[8]:

ab.some_attribute


# In[9]:

ba.some_attribute


# Reference:
# - Pro Python

# [Home](https://yang-zhang.github.io/)
