
# coding: utf-8

# `property` in Python

# In[142]:

class Dog:
    def __init__(self, weight):
        self.weight = weight


# In[143]:

dog = Dog(5)
dog.weight


# Someone can create a dog with negative weight, not good.

# In[144]:

dog = Dog(-5)
dog.weight


# You can use a setter to prevent people from creating negative-weight dogs.

# In[145]:

class Dog:
    def __init__(self, weight):
        self.set_weight(weight)
    
    def set_weight(self, weight):
        if weight <= 0:
            raise ValueError("Weight must be positive!")
        else:
            self.weight = weight


# In[146]:

dog = Dog(5)


# In[147]:

dog = Dog(-5)


# But you can't prevent people from setting good dogs' weight negative. 

# In[148]:

dog = Dog(5)
dog.weight = -5
dog.weight


# For this you can make use `property`.

# In[149]:

class Celsius:
    def __init__(self, temperature = 0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    def get_temperature(self):
        print("Getting value")
        return self._temperature

    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value

    temperature = property(get_temperature,set_temperature)


# In[150]:

class Dog:
    def __init__(self, weight):
        self.set_weight(weight)
    
    def set_weight(self, weight):
        if weight <= 0:
            raise ValueError("Weight must be positive!")
        self.weight = weight
    weight = property(fset=set_weight)


# In[151]:

dog = Dog(-5)


# In[152]:

dog = Dog(5)
dog.weight = -5


# As syntatic sugar, you can use the `@property` decorator.

# In[157]:

class Dog:
    def __init__(self, weight):
        self._weight = weight
        
    @property
    def weight(self):
        print("Get weight")
        return self._weight

    @weight.setter
    def weight(self, value):
        print("Set weight")
        if value <= 0:
            raise ValueError("Weight must be positive!")
        self._weight = value    


# In[158]:

dog = Dog(5)


# In[159]:

dog.weight


# In[160]:

dog.weight = 5


# In[161]:

dog.weight = -5


# However this does not prevent **creating** negative-weight dogs...

# In[163]:

dog = Dog(-5)
dog.weight


# In[164]:

dog.weight = -5


# References:
# - https://www.programiz.com/python-programming/property

# [Home](https://yang-zhang.github.io/)
