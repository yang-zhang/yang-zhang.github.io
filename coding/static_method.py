
# coding: utf-8

# In[ ]:




# In[116]:

class A(object):
    def foo(self, x):
        print("executing foo(%s, %s)" % (self, x))
    
    @classmethod
    def class_foo(cls, x):
        print("executing class_foo(%s, %s)" % (cls, x))
    
    @staticmethod
    def static_foo(x):
        print("executing static_foo(%s)" % (x))
    
    def bare_foo(x):
        print("executing bare_foo(%s)" % (x))


# In[117]:

a = A()


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

a.bare_foo(1)


# In[127]:

a.bare_foo()


# In[129]:

A.bare_foo(1)


# - Java for Python Programmers
# - https://stackoverflow.com/questions/136097/what-is-the-difference-between-staticmethod-and-classmethod-in-python

# [Home](https://yang-zhang.github.io/)
