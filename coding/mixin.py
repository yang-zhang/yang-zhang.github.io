
# coding: utf-8

# # Mixins in Python

# When accessing a non-existing attribute, and `AttributeError` is raised.

# In[14]:

class BaseClass:
    def __init__(self):
        self.some_attribute = "Im an attribute"


# In[15]:

b = BaseClass()
b.some_attribute


# In[16]:

b.non_existing_attribute


# In[19]:

b.__getattribute__('some_attribute')


# A mixin that returns `None` when you try to access non-existing attributes. 

# In[3]:

class NoneAttributes:
    def __getattr__(self, name):
        return None
    
class Example(BaseClass, NoneAttributes):
    pass

e = Example()
e.some_attribute


# In[11]:

e.non_existing_attribute


# In[10]:

e.non_existing_attribute is None


# In this example, it does not matter if `BaseClass` is before or after `NoneAttributes`.

# In[4]:

class OtherExample(NoneAttributes, BaseClass):
    pass
oe = OtherExample()


# In[24]:

oe.some_attribute


# The above is because `__getattr__` is only invoked if the attribute wasn't found the usual ways.

# In[5]:

oe.non_existing_attribute is None


# Reference:
# - Pro Python
# - https://stackoverflow.com/questions/3278077/difference-between-getattr-vs-getattribute

# [Home](https://yang-zhang.github.io/)
