
# coding: utf-8

# # Graph

# In[1]:

from inspect import getsourcelines

import graph_func
from importlib import reload
reload(graph_func)
from graph_func import nodes_from_network, connectivity, connections_of_each_node, connections_2nd_degree, print_source


# In[2]:

network = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
         (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]


# In[3]:

print_source(nodes_from_network)


# In[4]:

nodes = nodes_from_network(network)
nodes


# In[5]:

print_source(connectivity)


# In[6]:

connectivity(network)


# In[7]:

connections = connections_of_each_node(network)

connections


# Find 2nd-degree connections and number of common connections (friend of friend)

# In[8]:

for i in range(10):
    print(i, connections_2nd_degree(network, i))

