
# coding: utf-8

# http://www.pythonchallenge.com/

# In[1]:

2**38


# In[64]:

riddle = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""


# In[68]:

def decode(riddle):
    print(''.join([chr(((ord(letter)-ord_a+2) % 26) + ord_a) if ord('a')<=ord(letter)<=ord('z') else letter for letter in riddle]))


# In[69]:

decode(riddle)


# In[71]:

decode('map')


# In[75]:

ls


# In[ ]:




# In[ ]:




# In[ ]:



