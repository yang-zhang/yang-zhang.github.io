
# coding: utf-8

# # Table of Contents
#  <p><div class="lev1 toc-item"><a href="#My-&quot;complete&quot;-numpy.newaxis-notebook" data-toc-modified-id="My-&quot;complete&quot;-numpy.newaxis-notebook-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>My "complete" <code>numpy.newaxis</code> notebook</a></div><div class="lev2 toc-item"><a href="#0-D" data-toc-modified-id="0-D-11"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>0-D</a></div><div class="lev3 toc-item"><a href="#0-D-to-1-D" data-toc-modified-id="0-D-to-1-D-111"><span class="toc-item-num">1.1.1&nbsp;&nbsp;</span>0-D to 1-D</a></div><div class="lev3 toc-item"><a href="#0-D-to-2-D" data-toc-modified-id="0-D-to-2-D-112"><span class="toc-item-num">1.1.2&nbsp;&nbsp;</span>0-D to 2-D</a></div><div class="lev2 toc-item"><a href="#1-D" data-toc-modified-id="1-D-12"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>1-D</a></div><div class="lev3 toc-item"><a href="#1-D-to-2-D" data-toc-modified-id="1-D-to-2-D-121"><span class="toc-item-num">1.2.1&nbsp;&nbsp;</span>1-D to 2-D</a></div><div class="lev2 toc-item"><a href="#2-D" data-toc-modified-id="2-D-13"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>2-D</a></div><div class="lev4 toc-item"><a href="#2-D-to-3-D" data-toc-modified-id="2-D-to-3-D-1301"><span class="toc-item-num">1.3.0.1&nbsp;&nbsp;</span>2-D to 3-D</a></div>

# # My "complete" `numpy.newaxis` notebook

# In[39]:

from numpy import array, newaxis, expand_dims


# In[40]:

def show_array(y):
    print('array:', y)
    print('array.ndim:', y.ndim)
    print('array.shape:', y.shape)


# ## 0-D

# In[41]:

x = array(5)
show_array(x)


# ### 0-D to 1-D

# In[42]:

y = array(x)[newaxis]
show_array(y)


# In[43]:

y = np.expand_dims(x, axis=0)
show_array(y)


# Any number >= 0 does the same.

# In[44]:

y = np.expand_dims(x, axis=123456)
show_array(y)


# In[45]:

y = x.reshape(-1,)
show_array(y)


# ### 0-D to 2-D

# In[46]:

y = array(x)[newaxis, newaxis]
show_array(y)


# In[47]:

y = np.expand_dims(x, axis=0)
y = np.expand_dims(y, axis=0)
show_array(y)


# In[48]:

y = x.reshape(-1, 1)
show_array(y)


# ## 1-D

# In[49]:

x = array([5, 6, 7])
show_array(x)


# ### 1-D to 2-D

# ##### Vector to row matrix

# In[50]:

y = array(x)[newaxis, :]
show_array(y)


# In[51]:

y = array(x)[newaxis] # This is short hand of y = array(x)[newaxis, :]
show_array(y)


# In[52]:

y = np.expand_dims(x, axis=0)
show_array(y)


# In[53]:

y = x.reshape(1, -1)
show_array(y)


# ##### Vector to column matrix

# In[54]:

y = array(x)[:, newaxis]
show_array(y)


# In[55]:

y = np.expand_dims(x, axis=1)
show_array(y)


# Any number >= 1 does the same.

# In[56]:

y = np.expand_dims(x, axis=123456)
show_array(y)


# In[57]:

y = x.reshape(-1, 1)
show_array(y)


# ## 2-D

# In[58]:

x = array([[1, 2, 3], [4, 5, 6]])
show_array(x)


# #### 2-D to 3-D

# ##### Case 1

# In[59]:

y = array(x)[newaxis, :, :]
show_array(y)


# In[60]:

y = array(x)[newaxis, :]
show_array(y)


# In[61]:

y = array(x)[newaxis]
show_array(y)


# In[62]:

y = np.expand_dims(x, axis=0)
show_array(y)


# In[63]:

y = x.reshape(-1, 2, 3)
show_array(y)


# In[64]:

y = x.reshape(-1, *x.shape)
show_array(y)


# ##### Case 2

# In[65]:

y = array(x)[:, newaxis, :]
show_array(y)


# In[66]:

y = array(x)[:, newaxis]
show_array(y)


# In[67]:

y = np.expand_dims(x, axis=1)
show_array(y)


# In[68]:

y = x.reshape(2, 1, 3)
show_array(y)


# In[69]:

y = x.reshape(x.shape[0], -1, x.shape[1])
show_array(y)


# ##### Case 3

# In[70]:

y = array(x)[:, :, newaxis]
show_array(y)


# In[71]:

y = np.expand_dims(x, axis=2)
show_array(y)


# Any number >= 2 does the same.

# In[72]:

y = np.expand_dims(x, axis=123456)
show_array(y)


# In[73]:

y = x.reshape(*x.shape, -1)
show_array(y)

