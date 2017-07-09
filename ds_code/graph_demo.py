
# coding: utf-8

# # Graph functions in basic Python

# Some basic graph functions using basic python.

# In[1]:

from inspect import getsourcelines

import graph_func; from importlib import reload; reload(graph_func)
from graph_func import nodes_from_network, connectivity, connections_of_each_node, connections_2nd_degree, print_source


# Network: a list of tuples as edges of the network.

# In[2]:

network = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
         (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]


# ## Find all nodes in a network

# In[3]:

print_source(nodes_from_network)


# In[4]:

nodes = nodes_from_network(network)
nodes


# ## Connectivity

# In[5]:

print_source(connectivity)


# In[6]:

connectivity(network)


# ## Connections of each node

# In[7]:

print_source(connections_of_each_node)


# In[8]:

connections = connections_of_each_node(network)

connections


# ## 2nd-degree connections
# 
# Find 2nd-degree connections and number of common connections (friend of friend)

# In[9]:

print_source(connections_2nd_degree)


# In[10]:

for i in range(10):
    print(i, connections_2nd_degree(network, i))

