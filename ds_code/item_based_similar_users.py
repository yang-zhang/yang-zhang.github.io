
# coding: utf-8

# # How to find item-based similar users

# Suppose you want to find for a given user, what other users are most similar based on shared items (e.g. interests).

# In[2]:

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


# In[3]:

from collections import defaultdict

ids_by_interest = defaultdict(list)
interests_by_id = defaultdict(list)

for item in interests:
    id_ = item[0]
    interest = item[1]
    interests_by_id[id_].append(interest)
    ids_by_interest[interest].append(id_)


# In[4]:

print('ids_by_interest:', dict(ids_by_interest))


# In[5]:

print('interests_by_id:', dict(interests_by_id))


# In[11]:

from collections import Counter
def num_shared_interests_of_other_ids(id_):
    other_ids_sharing_interests = []
    for interest in interests_by_id[id_]:
        for other_id in ids_by_interest[interest]:
            if other_id != id_:
                other_ids_sharing_interests.append(other_id)
    return Counter(other_ids_sharing_interests)


# In[13]:

for id_ in range(10):
    print(id_, dict(num_shared_interests_of_other_ids(id_)))


# Reference: 
# - https://github.com/joelgrus/data-science-from-scratch

# [Home](https://yang-zhang.github.io/)
