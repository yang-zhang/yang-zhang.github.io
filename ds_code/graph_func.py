from inspect import getsourcelines
from collections import Counter


def print_source(obj):
    print(''.join(getsourcelines(obj)[0]))


def nodes_from_network(network):
    """
    Gets nodes from network edges.
    :param network: a list of tuples as edges of the network.
    :return: nodes of the network.
    """
    nodes = set()
    for edge in network:
        nodes.add(edge[0])
        nodes.add(edge[1])
    return nodes


def connectivity(network):
    """
    Calculates connectivity of a network.
    :param network: a list of tuples as edges of the network.
    :return: connectivity of a network.
    """
    nodes = nodes_from_network(network)
    number_nodes = len(nodes)
    number_edges = len(set(network))
    number_edges_fully_connected_network = int(number_nodes * (number_nodes-1) / 2)
    return number_edges / number_edges_fully_connected_network


def connections_of_each_node(network):
    """
    Find 1st-degree connections of each node in a network.
    :param network: a list of tuples as edges of the network.
    :return: 1st-degree connections of each node in a network.
    """
    connections = dict()
    nodes = nodes_from_network(network)
    for node in nodes:
        connections[node] = []
    for edge in network:
        connections[edge[0]].append(edge[1])
        connections[edge[1]].append(edge[0])
    return connections


def connections_2nd_degree(network, node):
    """
    For the given node in a given network, finds each 2nd-degree connection and the number of shared nodes.
    :param network: a list of tuples as edges of the network.
    :param node: the node to find 2nd-degree connections for.
    :return: a Counter object with 2nd-degree connection as the key and number of shared nodes as the value.
    """
    connections = connections_of_each_node(network)
    connections_2nd = []
    for connection_1st in connections[node]:
        for connection_2nd in connections[connection_1st]:
            if connection_2nd != node and connection_2nd not in connections[node]:
                connections_2nd.append(connection_2nd)
    return Counter(connections_2nd)
