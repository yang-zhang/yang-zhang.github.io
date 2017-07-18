
# coding: utf-8

# # Hashing objects in Python

# By default objects are hashed based on memory locations.

# In[83]:

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# In[84]:

point1 = Point(1, 2)
point2 = Point(1, 2)


# In[85]:

hash(point1) == hash(point2)


# In[86]:

st = set([point1, point2])
point3 = Point(1, 2)
point3 in st


# Can implement customer `__hash__` and `__eq__` for more desirable behavior.

# In[87]:

class PointNew:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __hash__(self):
        return hash((self.x, self.y))
    def __eq__(self, other):
        return self.x==other.x and self.y==other.y
        


# In[88]:

point1 = PointNew(1, 2)
point2 = PointNew(1, 2)


# In[89]:

hash(point1) == hash(point2)


# In[90]:

id(point1), id(point2)


# In[91]:

st = set([point1, point2])
point3 = PointNew(1, 2)
point3 in st


# Reference:
# - High Performance Python

# [Home](https://yang-zhang.github.io/)
