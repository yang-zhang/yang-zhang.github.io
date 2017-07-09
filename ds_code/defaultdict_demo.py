
# coding: utf-8

# # When and how to use collections.defaultdict

# Suppose you want to build lookup tables of "interests by id" and "ids by interest" from this data.

# In[54]:

interests = [
        (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
        (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
        (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
        (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
        (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
        (3, "statistics"), (3, "regression"), (3, "probability"),
        (4, "machine learning"), (4, "regression"), (4, "decision trees"),
        (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
        (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
        (6, "probability"), (6, "mathematics"), (6, "theory"),
        (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
        (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
        (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
        (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]


# ## Use regular dict

# Need to handle new keys using regular dict

# In[55]:

ids_by_interest = {}
interests_by_id = {}

for item in interests:
    id_ = item[0]
    interest = item[1]
    
    if id_ in interests_by_id:
        interests_by_id[id_].append(interest)
    else:
        interests_by_id[id_] = [interest]
    
    if interest in ids_by_interest:
        ids_by_interest[interest].append(id_)
    else:
        ids_by_interest[interest] = [id_]


# In[56]:

print('ids_by_interest:', dict(ids_by_interest))


# In[57]:

print('interests_by_id:', dict(interests_by_id))


# ## Use defaultdict

# Using defaultdict can simplify the code.

# In[58]:

from collections import defaultdict

ids_by_interest = defaultdict(list)
interests_by_id = defaultdict(list)

for item in interests:
    id_ = item[0]
    interest = item[1]
    interests_by_id[id_].append(interest)
    ids_by_interest[interest].append(id_)


# In[59]:

print('ids_by_interest:', dict(ids_by_interest))


# In[60]:

print('interests_by_id:', dict(interests_by_id))


# Reference: 
# - https://github.com/joelgrus/data-science-from-scratch

# [Home](https://yang-zhang.github.io/)
