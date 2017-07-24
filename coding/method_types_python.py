
# coding: utf-8

# # Instance method, class method, and static method in Python

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


# ## Regular instance method
# `foo(self, x)` is a regular object method. 

# In[140]:

a.foo(1)


# When `foo` is called by the class `A`, `self` (the object instance) is not passed to `foo`, causing an error.

# In[141]:

A.foo(1)


# This fabricated case allows `A` to call `foo` in unintened way.

# In[142]:

A.foo(1, 1)


# ## `@classmethod`
# `class_foo(cls, x)` is a `@classmethod`. The class is passed to foo as the first argument.

# In[143]:

a.class_foo(1)


# In[144]:

A.class_foo(1)


# ## @staticmethod
# `static_foo(x)` is a `@staticmethod`. It can be called by the object and the class without passing the object instance or the class.

# In[145]:

a.static_foo(1)


# In[146]:

A.static_foo(1)


# ## An odd case
# `foo2(x)` is the same as `foo2(self)` expect using an unconventional name `x` instead of `self`.

# In[147]:

a.foo2(1)


# In[148]:

a.foo2()


# This fabricated case allows `A` to call `foo2` in unintened way.

# In[149]:

A.foo2(1)


# ## An other odd case
# `foo3()` fails to define argument `self` therefore cannot be called by `a` because `a` will pass it the object instance (i.e., `a` it`self`).

# In[138]:

a.foo3()


# This fabricated case allows `A` to call `foo2` in unintened way.

# In[150]:

A.foo3()


# - Java for Python Programmers
# - https://stackoverflow.com/questions/136097/what-is-the-difference-between-staticmethod-and-classmethod-in-python

# [Home](https://yang-zhang.github.io/)
