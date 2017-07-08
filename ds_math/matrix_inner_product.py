
# coding: utf-8

# # Matrix inner product demo

# In[73]:

import numpy as np


# In[74]:

X = np.array([[1, 2, 3], [4, 5, 6]])

Y = np.array([[7, 8, 9], [10, 11, 12]])


# In[75]:

X


# In[76]:

Y


# In[77]:

m, n = X.shape[0], Y.shape[1]

inner_product = 0
for i in range(m):
    for j in range(n):
        print('X[i,j] * Y[i,j] = ', X[i,j] , '*', Y[i,j])
        inner_product += X[i,j] * Y[i,j]
inner_product


# In[78]:

prdct = np.dot(X.T, Y)

prdct


# In[79]:

np.trace(prdct)


# Trace is ths sum of the diagnal elements.

# In[80]:

tc = 0
for i in range(prdct.shape[0]):
    tc += prdct[i,i]
tc


# Reference: 
# - See pp.647 of Introduction to Linear Algebra, Fourth Edition 4th Edition by Gilbert Strang
# - https://en.wikipedia.org/wiki/Frobenius_inner_product
