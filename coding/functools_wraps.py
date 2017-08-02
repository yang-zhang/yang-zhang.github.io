
# coding: utf-8

# # Create decorator using `functools.wraps`

# In[13]:

def my_basic_decorator(func):
    def wrapper(*args, **kwargs):
        print('This is pure decoration!')
        return func(*args, **kwargs)
    return wrapper


# In[14]:

@my_basic_decorator
def my_sum(x, y):
    """Dis my sum!"""
    return x + y


# In[15]:

my_sum(1, 2)


# However this loss some information.

# In[16]:

my_sum.__doc__ is None


# In[17]:

my_sum


# A solution to this is `functools.wraps`.

# In[18]:

import functools


# In[19]:

def my_fancy_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('This is still pure decoration!')
        return func(*args, **kwargs)
    return wrapper


# In[20]:

@my_fancy_decorator
def my_fancy_sum(x, y):
    """Dis my fancy sum!"""
    return x + y


# In[21]:

my_fancy_sum(1, 2)


# In[22]:

my_fancy_sum


# In[23]:

my_fancy_sum.__doc__


# [Home](https://yang-zhang.github.io/)
