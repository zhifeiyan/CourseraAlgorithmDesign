###############################################
# Coursera algorithm design and analysis part I
# Programming assignment 3
# Karger's min cut algorithm
# Created by Zhifei Yan
###############################################

import random
import copy

def kargermincut(graph):
    """
    Karger's min cut algorithm
    graph: a dictionary of adjacency list
    Treat each node as a key, a list of its neighbors as value
    Return the number of crossing edges of the cut obtained
    """
    for i in range(len(graph) - 2):
        # randomly pick one edge
        start = random.choice(list(graph.keys()))
        end = random.choice(graph[start])
        # merge end node into start node
        for j in set(graph[end]):
            graph[j] = [n if n != end else start for n in graph[j]]
        # note that extend is in-place modification operation, return None
        graph[start].extend(graph[end])
        graph[start] = [n for n in graph[start] if n != start]
        del graph[end]
    return len(list(graph.values())[0])

if __name__ == '__main__':
    # read adjacency list as a dictionary
    graph = {}
    for line in open('kargermincut.txt'):
        temp = line.split()
        temp = [int(i) for i in temp]
        graph[temp[0]] = temp[1:]

    num_rep = 100
    k = 1e6
    for i in range(num_rep):
        graph_copy = copy.deepcopy(graph)
        k_new = kargermincut(graph_copy)
        if k_new < k:
            k = k_new
