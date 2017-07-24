
# coding: utf-8

# # Regular, `@staticmethod`, and `@classmethod` in Python

# In[136]:

class A(object):
    def foo(self, x):
        print("executing foo(%s, %s)" % (self, x))
    
    @classmethod
    def class_foo(cls, x):
        print("executing class_foo(%s, %s)" % (cls, x))
    
    @staticmethod
    def static_foo(x):
        print("executing static_foo(%s)" % (x))
    
    def foo2(x):
        print("executing foo2(%s)" % (x))
        
    def foo3():
        print("executing foo3")


# In[137]:

a = A()


# `foo()` is a regular object method. 

# In[118]:

a.foo(1)


# In[119]:

A.foo(1)


# In[131]:

A.foo(1, 1)


# In[120]:

a.class_foo(1)


# In[121]:

A.class_foo(1)


# In[122]:

a.static_foo(1)


# In[123]:

A.static_foo(1)


# In[124]:

a.foo2(1)


# In[127]:

a.foo2()


# In[129]:

A.foo2(1)


# In[138]:

a.foo3()


# In[139]:

A.foo3()


# - Java for Python Programmers
# - https://stackoverflow.com/questions/136097/what-is-the-difference-between-staticmethod-and-classmethod-in-python

# [Home](https://yang-zhang.github.io/)
