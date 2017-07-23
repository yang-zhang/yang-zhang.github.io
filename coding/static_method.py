
# coding: utf-8

# In[104]:

class Hello1(object):
    def main(self):
        print("Hello 1")


# In[105]:

Hello1.main()


# In[106]:

Hello1().main()


# In[101]:

class Hello2(object):
    @staticmethod
    def main():
        print("Hello 2")


# In[102]:

Hello2.main()


# In[103]:

Hello2().main()


# In[107]:

class Hello3(object):
    def main():
        print("Hello 3")


# In[108]:

Hello3.main()


# In[109]:

Hello3().main()

