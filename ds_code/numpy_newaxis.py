
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc" style="margin-top: 1em;"><ul class="toc-item"><li><span><a href="#Adding-dimensions-to-numpy.arrays:-newaxis-v.s.-reshape-v.s.-expand_dims" data-toc-modified-id="Adding-dimensions-to-numpy.arrays:-newaxis-v.s.-reshape-v.s.-expand_dims-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Adding dimensions to <code>numpy.arrays</code>: <code>newaxis</code> v.s. <code>reshape</code> v.s. <code>expand_dims</code></a></span><ul class="toc-item"><li><span><a href="#From-0-D-(scalar)-to-n-D" data-toc-modified-id="From-0-D-(scalar)-to-n-D-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>From 0-D (scalar) to n-D</a></span><ul class="toc-item"><li><span><a href="#From-0-D-to-1-D" data-toc-modified-id="From-0-D-to-1-D-1.1.1"><span class="toc-item-num">1.1.1&nbsp;&nbsp;</span>From 0-D to 1-D</a></span></li><li><span><a href="#From-0-D-to-2-D" data-toc-modified-id="From-0-D-to-2-D-1.1.2"><span class="toc-item-num">1.1.2&nbsp;&nbsp;</span>From 0-D to 2-D</a></span></li></ul></li><li><span><a href="#From-1-D-to-n-D-(n>1)" data-toc-modified-id="From-1-D-to-n-D-(n>1)-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>From 1-D to n-D (n&gt;1)</a></span><ul class="toc-item"><li><span><a href="#From-1-D-to-2-D" data-toc-modified-id="From-1-D-to-2-D-1.2.1"><span class="toc-item-num">1.2.1&nbsp;&nbsp;</span>From 1-D to 2-D</a></span></li></ul></li><li><span><a href="#From-2-D-to-n-D-(n>2)" data-toc-modified-id="From-2-D-to-n-D-(n>2)-1.3"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>From 2-D to n-D (n&gt;2)</a></span><ul class="toc-item"><li><span><a href="#2-D-to-3-D" data-toc-modified-id="2-D-to-3-D-1.3.1"><span class="toc-item-num">1.3.1&nbsp;&nbsp;</span>2-D to 3-D</a></span><ul class="toc-item"><li><span><a href="#Case-1-:-Add-newaxis-at-the-beginning" data-toc-modified-id="Case-1-:-Add-newaxis-at-the-beginning-1.3.1.1"><span class="toc-item-num">1.3.1.1&nbsp;&nbsp;</span>Case 1 : Add <code>newaxis</code> at the beginning</a></span></li><li><span><a href="#Case-2:--Squeeze-newaxis-in-the-middle" data-toc-modified-id="Case-2:--Squeeze-newaxis-in-the-middle-1.3.1.2"><span class="toc-item-num">1.3.1.2&nbsp;&nbsp;</span>Case 2:  Squeeze <code>newaxis</code> in the middle</a></span></li><li><span><a href="#Case-3:-Add-newaxis-to-the-end" data-toc-modified-id="Case-3:-Add-newaxis-to-the-end-1.3.1.3"><span class="toc-item-num">1.3.1.3&nbsp;&nbsp;</span>Case 3: Add <code>newaxis</code> to the end</a></span></li></ul></li></ul></li></ul></li></ul></div>

# In[123]:

from numpy import array, newaxis, expand_dims


# # Adding dimensions to `numpy.arrays`: `newaxis` v.s. `reshape` v.s. `expand_dims`

# This post demonstrates 3 ways to add new dimensions to numpy.arrays `usingnumpy.newaxis`, `reshape`, or `expand_dim`.
# 
# First define a display function. 

# In[124]:

def show_array(y):
    print('array: \n', y)
    print('array.ndim:', y.ndim)
    print('array.shape:', y.shape)


# ## From 0-D (scalar) to n-D

# In[125]:

x = array(5)
show_array(x)


# ### From 0-D to 1-D

# `y` is the result of adding a new dimension to `x`, and the shape is no longer empty.

# In[126]:

y = array(x)[newaxis]
show_array(y)


# Equivalently,

# In[127]:

y = expand_dims(x, axis=0)
show_array(y)


# Any number >= 0 does the same as the above.

# In[128]:

y = expand_dims(x, axis=123456)
show_array(y)


# Also equivalently,

# In[129]:

y = x.reshape(-1,)
show_array(y)


# ### From 0-D to 2-D

# In[130]:

y = array(x)[newaxis, newaxis]
show_array(y)


# In[131]:

y = expand_dims(x, axis=0)
z = expand_dims(y, axis=0)
show_array(z)


# In[132]:

y = x.reshape(-1, 1)
show_array(y)


# ## From 1-D to n-D (n>1)

# In[133]:

x = array([5, 6, 7])
show_array(x)


# ### From 1-D to 2-D

# ##### Vector to row matrix

# Adding `newaxis` at the beginning changes the shape from `(3,)` to `(1, 3)`.

# In[134]:

y = array(x)[newaxis, :]
show_array(y)


# In[135]:

y = array(x)[newaxis] # This is short hand of y = array(x)[newaxis, :]
show_array(y)


# In[136]:

y = expand_dims(x, axis=0)
show_array(y)


# In[137]:

y = x.reshape(1, -1)
show_array(y)


# ##### Vector to column matrix

# Adding `newaxis` at the end changes the shape from `(3,)` to `(3, 1)`.

# In[138]:

y = array(x)[:, newaxis]
show_array(y)


# In[139]:

y = expand_dims(x, axis=1)
show_array(y)


# Equivalently,

# In[140]:

y = expand_dims(x, axis=-1)
show_array(y)


# Any number >= 1 does the same.

# In[141]:

y = expand_dims(x, axis=123456)
show_array(y)


# In[142]:

y = x.reshape(-1, 1)
show_array(y)


# ## From 2-D to n-D (n>2)

# In[143]:

x = array([[1, 2, 3], [4, 5, 6]])
show_array(x)


# ### 2-D to 3-D

# #### Case 1 : Add `newaxis` at the beginning

# In[144]:

y = array(x)[newaxis, :, :]
show_array(y)


# Equivalently,

# In[145]:

y = array(x)[newaxis, :]
show_array(y)


# Equivalently,

# In[146]:

y = array(x)[newaxis]
show_array(y)


# In[147]:

y = expand_dims(x, axis=0)
show_array(y)


# In[148]:

y = x.reshape(-1, 2, 3)
show_array(y)


# In[149]:

y = x.reshape(-1, *x.shape)
show_array(y)


# #### Case 2:  Squeeze `newaxis` in the middle

# In[150]:

y = array(x)[:, newaxis, :]
show_array(y)


# In[151]:

y = array(x)[:, newaxis]
show_array(y)


# In[152]:

y = expand_dims(x, axis=1)
show_array(y)


# In[153]:

y = x.reshape(2, 1, 3)
show_array(y)


# In[154]:

y = x.reshape(x.shape[0], -1, x.shape[1])
show_array(y)


# #### Case 3: Add `newaxis` to the end

# In[155]:

y = array(x)[:, :, newaxis]
show_array(y)


# In[156]:

y = expand_dims(x, axis=2)
show_array(y)


# In[157]:

y = expand_dims(x, axis=-1)
show_array(y)


# Any number >= 2 does the same.

# In[158]:

y = expand_dims(x, axis=123456)
show_array(y)


# In[159]:

y = x.reshape(*x.shape, -1)
show_array(y)


# [Home](https://yang-zhang.github.io/)
