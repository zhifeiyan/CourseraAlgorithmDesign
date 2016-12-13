###############################################
# Coursera algorithm design and analysis part I
# Programming assignment 5
# Dijkstra's shortest-path algorithm
# This implementation uses heap data structure provided by heapq module
# TODO: add O(log n) deletion method to heap
# Created by Zhifei Yan
###############################################

import heapq

def shortestpath(graph, source=1, max_dist=10**6):
    # placeholder for shortest-path distance
    shortest_dist = {source:0}
    # initialization
    heap = []
    heap.extend(list(zip(graph[source].values(), graph[source].keys())))
    for i in graph.keys() - {source} - graph[source].keys():
        heap.append((max_dist, i))
    heapq.heapify(heap)

    while len(heap) != 0:
        mindist, node = heapq.heappop(heap)
        shortest_dist[node] = mindist
        # check edges linked to newly processed node
        nodedict = graph[node]
        for v in nodedict:
            if v not in shortest_dist:
                for i, (olddist, n_id) in enumerate(heap):
                    if n_id == v:
                        del heap[i]
                        break
                newdist = min(olddist, mindist + nodedict[v])
                heap.append((newdist, v))
        heapq.heapify(heap)
    return shortest_dist

if __name__ == '__main__':
    # read adjacency list as a dictionary of dictionaries
    graph = {}
    for line in open('shortestpath.txt'):
        line = line.split()
        graph[int(line[0])] = {int(i.split(',')[0]):int(i.split(',')[1]) for i in line[1:]}
    shortest_dist = shortestpath(graph)
    res_node = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
    for i in res_node:
        print(shortest_dist[i])
