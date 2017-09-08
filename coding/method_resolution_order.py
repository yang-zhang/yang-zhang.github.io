
# coding: utf-8

# # Method Resolution Order (MRO) in Python

# ## Vertical

# In[8]:

class A:
    def func_1(self):
        print('Func 1 A')
    def func_2(self):
        print('Func 2 A')

class B(A):
    pass

class C(B):
    def func_1(self):
        print('Func 1 C')


# In[9]:

a = A()
b = B()
c = C()


# In[11]:

a.func_1()
a.func_2()


# In[12]:

b.func_1()
b.func_2()


# In[13]:

c.func_1()
c.func_2()


# ## Horizontal

# In[14]:

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


# In[15]:

ab.some_attribute


# In[16]:

ba.some_attribute


# ## Mixed

# In[ ]:




# Reference:
# - Pro Python

# [Home](https://yang-zhang.github.io/)
