
# coding: utf-8

# # Table of Contents
#  <p><div class="lev1 toc-item"><a href="#A-relatively-complete-demo-of-reshaping-numpy.arrays-using-newaxis,-reshape,-or-expand_dims" data-toc-modified-id="A-relatively-complete-demo-of-reshaping-numpy.arrays-using-newaxis,-reshape,-or-expand_dims-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>A relatively complete demo of reshaping <code>numpy.arrays</code> using <code>newaxis</code>, <code>reshape</code>, or <code>expand_dims</code></a></div><div class="lev2 toc-item"><a href="#From-0-D" data-toc-modified-id="From-0-D-11"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>From 0-D</a></div><div class="lev3 toc-item"><a href="#From-0-D-to-1-D" data-toc-modified-id="From-0-D-to-1-D-111"><span class="toc-item-num">1.1.1&nbsp;&nbsp;</span>From 0-D to 1-D</a></div><div class="lev3 toc-item"><a href="#From-0-D-to-2-D" data-toc-modified-id="From-0-D-to-2-D-112"><span class="toc-item-num">1.1.2&nbsp;&nbsp;</span>From 0-D to 2-D</a></div><div class="lev2 toc-item"><a href="#From-1-D" data-toc-modified-id="From-1-D-12"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>From 1-D</a></div><div class="lev3 toc-item"><a href="#From-1-D-to-2-D" data-toc-modified-id="From-1-D-to-2-D-121"><span class="toc-item-num">1.2.1&nbsp;&nbsp;</span>From 1-D to 2-D</a></div><div class="lev2 toc-item"><a href="#2-D" data-toc-modified-id="2-D-13"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>2-D</a></div><div class="lev4 toc-item"><a href="#2-D-to-3-D" data-toc-modified-id="2-D-to-3-D-1301"><span class="toc-item-num">1.3.0.1&nbsp;&nbsp;</span>2-D to 3-D</a></div>

# # A relatively complete demo of reshaping `numpy.arrays` using `newaxis`, `reshape`, or `expand_dims`

# Reshaping `numpy.arrays` with the choices of `numpy.newaxis`, `reshape`, and `expand_dims` could be confusing sometimes. Making the three do the same thing helps to demonstrate how they work. Looking at `ndim` and `shape` also helps.

# In[37]:

from numpy import array, newaxis, expand_dims


# In[38]:

def show_array(y):
    print('array: \n', y)
    print('array.ndim:', y.ndim)
    print('array.shape:', y.shape)


# ## From 0-D

# In[39]:

x = array(5)
show_array(x)


# ### From 0-D to 1-D

# `y` is the result of adding a new dimension to `x`, and the shape is no longer empty.

# In[56]:

y = array(x)[newaxis]
show_array(y)


# Equivalently,

# In[57]:

y = expand_dims(x, axis=0)
show_array(y)


# Any number >= 0 does the same as the above.

# In[62]:

y = expand_dims(x, axis=123456)
show_array(y)


# Also equivalently,

# In[61]:

y = x.reshape(-1,)
show_array(y)


# ### From 0-D to 2-D

# In[44]:

y = array(x)[newaxis, newaxis]
show_array(y)


# In[45]:

y = expand_dims(x, axis=0)
z = expand_dims(y, axis=0)
show_array(z)


# In[54]:

y = x.reshape(-1, 1)
show_array(y)


# ## From 1-D

# In[11]:

x = array([5, 6, 7])
show_array(x)


# ### From 1-D to 2-D

# ##### Vector to row matrix

# Adding `newaxis` at the beginning changes the shape from `(3,)` to `(1, 3)`.

# In[12]:

y = array(x)[newaxis, :]
show_array(y)


# In[13]:

y = array(x)[newaxis] # This is short hand of y = array(x)[newaxis, :]
show_array(y)


# In[14]:

y = expand_dims(x, axis=0)
show_array(y)


# In[15]:

y = x.reshape(1, -1)
show_array(y)


# ##### Vector to column matrix

# Adding `newaxis` at the end changes the shape from `(3,)` to `(3, 1)`.

# In[16]:

y = array(x)[:, newaxis]
show_array(y)


# In[17]:

y = expand_dims(x, axis=1)
show_array(y)


# Any number >= 1 does the same.

# In[18]:

y = expand_dims(x, axis=123456)
show_array(y)


# In[19]:

y = x.reshape(-1, 1)
show_array(y)


# ## 2-D

# In[20]:

x = array([[1, 2, 3], [4, 5, 6]])
show_array(x)


# #### 2-D to 3-D

# ##### Case 1

# Adding `newaxis` at the beginning.

# In[21]:

y = array(x)[newaxis, :, :]
show_array(y)


# In[22]:

y = array(x)[newaxis, :]
show_array(y)


# In[23]:

y = array(x)[newaxis]
show_array(y)


# In[24]:

y = expand_dims(x, axis=0)
show_array(y)


# In[25]:

y = x.reshape(-1, 2, 3)
show_array(y)


# In[26]:

y = x.reshape(-1, *x.shape)
show_array(y)


# ##### Case 2

# Squeaze `newaxis` in the middle.

# In[27]:

y = array(x)[:, newaxis, :]
show_array(y)


# In[28]:

y = array(x)[:, newaxis]
show_array(y)


# In[29]:

y = expand_dims(x, axis=1)
show_array(y)


# In[30]:

y = x.reshape(2, 1, 3)
show_array(y)


# In[31]:

y = x.reshape(x.shape[0], -1, x.shape[1])
show_array(y)


# ##### Case 3

# Adding `newaxis` to the end.

# In[32]:

y = array(x)[:, :, newaxis]
show_array(y)


# In[33]:

y = expand_dims(x, axis=2)
show_array(y)


# Any number >= 2 does the same.

# In[34]:

y = expand_dims(x, axis=123456)
show_array(y)


# In[35]:

y = x.reshape(*x.shape, -1)
show_array(y)


# [Home](https://yang-zhang.github.io/)
