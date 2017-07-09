from inspect import getsourcelines
from collections import Counter

def print_source(obj):
    print(''.join(getsourcelines(obj)[0]))


def nodes_from_network(network):
    nodes = set()
    for edge in network:
        nodes.add(edge[0])
        nodes.add(edge[1])
    return nodes


def connectivity(network):
    nodes = nodes_from_network(network)
    number_nodes = len(nodes)
    number_edges = len(set(network))
    number_edges_fully_connected_network = int(number_nodes * (number_nodes-1) / 2)
    return number_edges / number_edges_fully_connected_network


def connections_of_each_node(network):
    connections = dict()
    nodes = nodes_from_network(network)
    for node in nodes:
        connections[node] = []
    for edge in network:
        connections[edge[0]].append(edge[1])
        connections[edge[1]].append(edge[0])
    return connections


def connections_2nd_degree(network, node):
    connections = connections_of_each_node(network)
    connections_2nd = []
    for connection_1st in connections[node]:
        for connection_2nd in connections[connection_1st]:
            if connection_2nd!=node and connection_2nd not in connections[node]:
                connections_2nd.append(connection_2nd)

    return Counter(connections_2nd)