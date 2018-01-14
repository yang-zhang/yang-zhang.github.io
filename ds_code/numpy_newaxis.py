
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc" style="margin-top: 1em;"><ul class="toc-item"><li><span><a href="#Adding-dimensions-to-numpy.arrays:-newaxis-v.s.-reshape-v.s.-expand_dims" data-toc-modified-id="Adding-dimensions-to-numpy.arrays:-newaxis-v.s.-reshape-v.s.-expand_dims-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Adding dimensions to <code>numpy.arrays</code>: <code>newaxis</code> v.s. <code>reshape</code> v.s. <code>expand_dims</code></a></span><ul class="toc-item"><li><span><a href="#From-0-D" data-toc-modified-id="From-0-D-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>From 0-D</a></span><ul class="toc-item"><li><span><a href="#From-0-D-to-1-D" data-toc-modified-id="From-0-D-to-1-D-1.1.1"><span class="toc-item-num">1.1.1&nbsp;&nbsp;</span>From 0-D to 1-D</a></span></li><li><span><a href="#From-0-D-to-2-D" data-toc-modified-id="From-0-D-to-2-D-1.1.2"><span class="toc-item-num">1.1.2&nbsp;&nbsp;</span>From 0-D to 2-D</a></span></li></ul></li><li><span><a href="#From-1-D" data-toc-modified-id="From-1-D-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>From 1-D</a></span><ul class="toc-item"><li><span><a href="#From-1-D-to-2-D" data-toc-modified-id="From-1-D-to-2-D-1.2.1"><span class="toc-item-num">1.2.1&nbsp;&nbsp;</span>From 1-D to 2-D</a></span></li></ul></li><li><span><a href="#2-D" data-toc-modified-id="2-D-1.3"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>2-D</a></span><ul class="toc-item"><li><ul class="toc-item"><li><span><a href="#2-D-to-3-D" data-toc-modified-id="2-D-to-3-D-1.3.0.1"><span class="toc-item-num">1.3.0.1&nbsp;&nbsp;</span>2-D to 3-D</a></span></li></ul></li></ul></li></ul></li></ul></div>

# # Adding dimensions to `numpy.arrays`: `newaxis` v.s. `reshape` v.s. `expand_dims`

# This notebook demonstrates 3 ways to add new dimensions to numpy.arrays `usingnumpy.newaxis`, `reshape`, or `expand_dim`.

# In[1]:

from numpy import array, newaxis, expand_dims

def show_array(y):
    print('array: \n', y)
    print('array.ndim:', y.ndim)
    print('array.shape:', y.shape)


# ## From 0-D

# In[2]:

x = array(5)
show_array(x)


# ### From 0-D to 1-D

# `y` is the result of adding a new dimension to `x`, and the shape is no longer empty.

# In[3]:

y = array(x)[newaxis]
show_array(y)


# Equivalently,

# In[4]:

y = expand_dims(x, axis=0)
show_array(y)


# Any number >= 0 does the same as the above.

# In[8]:

y = expand_dims(x, axis=123456)
show_array(y)


# Also equivalently,

# In[9]:

y = x.reshape(-1,)
show_array(y)


# ### From 0-D to 2-D

# In[10]:

y = array(x)[newaxis, newaxis]
show_array(y)


# In[11]:

y = expand_dims(x, axis=0)
z = expand_dims(y, axis=0)
show_array(z)


# In[12]:

y = x.reshape(-1, 1)
show_array(y)


# ## From 1-D

# In[13]:

x = array([5, 6, 7])
show_array(x)


# ### From 1-D to 2-D

# ##### Vector to row matrix

# Adding `newaxis` at the beginning changes the shape from `(3,)` to `(1, 3)`.

# In[14]:

y = array(x)[newaxis, :]
show_array(y)


# In[15]:

y = array(x)[newaxis] # This is short hand of y = array(x)[newaxis, :]
show_array(y)


# In[16]:

y = expand_dims(x, axis=0)
show_array(y)


# In[17]:

y = x.reshape(1, -1)
show_array(y)


# ##### Vector to column matrix

# Adding `newaxis` at the end changes the shape from `(3,)` to `(3, 1)`.

# In[18]:

y = array(x)[:, newaxis]
show_array(y)


# In[19]:

y = expand_dims(x, axis=1)
show_array(y)


# Any number >= 1 does the same.

# In[20]:

y = expand_dims(x, axis=123456)
show_array(y)


# In[21]:

y = x.reshape(-1, 1)
show_array(y)


# ## 2-D

# In[22]:

x = array([[1, 2, 3], [4, 5, 6]])
show_array(x)


# #### 2-D to 3-D

# ##### Case 1

# Adding `newaxis` at the beginning.

# In[23]:

y = array(x)[newaxis, :, :]
show_array(y)


# In[24]:

y = array(x)[newaxis, :]
show_array(y)


# In[25]:

y = array(x)[newaxis]
show_array(y)


# In[26]:

y = expand_dims(x, axis=0)
show_array(y)


# In[27]:

y = x.reshape(-1, 2, 3)
show_array(y)


# In[28]:

y = x.reshape(-1, *x.shape)
show_array(y)


# ##### Case 2

# Squeaze `newaxis` in the middle.

# In[29]:

y = array(x)[:, newaxis, :]
show_array(y)


# In[30]:

y = array(x)[:, newaxis]
show_array(y)


# In[31]:

y = expand_dims(x, axis=1)
show_array(y)


# In[32]:

y = x.reshape(2, 1, 3)
show_array(y)


# In[33]:

y = x.reshape(x.shape[0], -1, x.shape[1])
show_array(y)


# ##### Case 3

# Adding `newaxis` to the end.

# In[34]:

y = array(x)[:, :, newaxis]
show_array(y)


# In[35]:

y = expand_dims(x, axis=2)
show_array(y)


# Any number >= 2 does the same.

# In[36]:

y = expand_dims(x, axis=123456)
show_array(y)


# In[37]:

y = x.reshape(*x.shape, -1)
show_array(y)


# [Home](https://yang-zhang.github.io/)
