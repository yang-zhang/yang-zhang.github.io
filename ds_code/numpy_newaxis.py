
# coding: utf-8

# # Table of Contents
#  <p><div class="lev1 toc-item"><a href="#My-&quot;complete&quot;-numpy.newaxis-notebook" data-toc-modified-id="My-&quot;complete&quot;-numpy.newaxis-notebook-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>My "complete" <code>numpy.newaxis</code> notebook</a></div><div class="lev2 toc-item"><a href="#0-D" data-toc-modified-id="0-D-11"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>0-D</a></div><div class="lev3 toc-item"><a href="#0-D-to-1-D" data-toc-modified-id="0-D-to-1-D-111"><span class="toc-item-num">1.1.1&nbsp;&nbsp;</span>0-D to 1-D</a></div><div class="lev3 toc-item"><a href="#0-D-to-2-D" data-toc-modified-id="0-D-to-2-D-112"><span class="toc-item-num">1.1.2&nbsp;&nbsp;</span>0-D to 2-D</a></div><div class="lev2 toc-item"><a href="#1-D" data-toc-modified-id="1-D-12"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>1-D</a></div><div class="lev3 toc-item"><a href="#1-D-to-2-D" data-toc-modified-id="1-D-to-2-D-121"><span class="toc-item-num">1.2.1&nbsp;&nbsp;</span>1-D to 2-D</a></div><div class="lev2 toc-item"><a href="#2-D" data-toc-modified-id="2-D-13"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>2-D</a></div><div class="lev4 toc-item"><a href="#2-D-to-3-D" data-toc-modified-id="2-D-to-3-D-1301"><span class="toc-item-num">1.3.0.1&nbsp;&nbsp;</span>2-D to 3-D</a></div>

# # My "complete" `numpy.newaxis` demo

# In[1]:

from numpy import array, newaxis, expand_dims


# In[2]:

def show_array(y):
    print('array: \n', y)
    print('array.ndim:', y.ndim)
    print('array.shape:', y.shape)


# ## 0-D

# In[3]:

x = array(5)
show_array(x)


# ### 0-D to 1-D

# In[4]:

y = array(x)[newaxis]
show_array(y)


# In[5]:

y = expand_dims(x, axis=0)
show_array(y)


# Any number >= 0 does the same.

# In[6]:

y = expand_dims(x, axis=123456)
show_array(y)


# In[7]:

y = x.reshape(-1,)
show_array(y)


# ### 0-D to 2-D

# In[8]:

y = array(x)[newaxis, newaxis]
show_array(y)


# In[9]:

y = expand_dims(x, axis=0)
y = expand_dims(y, axis=0)
show_array(y)


# In[10]:

y = x.reshape(-1, 1)
show_array(y)


# ## 1-D

# In[11]:

x = array([5, 6, 7])
show_array(x)


# ### 1-D to 2-D

# ##### Vector to row matrix

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

