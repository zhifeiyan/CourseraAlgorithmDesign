###############################################
# Coursera algorithm design and analysis part I
# Programming assignment 4
# Kosaraju’s two-pass algorithm of finding strongly connected components
# Created by Zhifei Yan
###############################################

from collections import defaultdict, Counter
import sys
import resource
sys.setrecursionlimit(10 ** 6)
resource.setrlimit(resource.RLIMIT_STACK, (2 ** 29, 2 ** 30))

def dfs_loop(graph, n, f_cur=None):
    """
    visited: a boolean list, pad the first element using None
    f_cur: a list of finishing time of each node, pad the first element using None
    """
    f_new = [None] * (n + 1)
    leader_list = [None] * (n + 1)
    visited = [False] * (n + 1)

    for i in range(n, 0, -1):
        v_id = i
        if f_cur is not None:
            v_id = f_cur.index(i)
        if not visited[v_id]:
            # leader is the very first node (v_id) that triggers a seq of recursive DFS calls
            dfs(graph, v_id, f_new, leader_list, visited, v_id)
    return f_new, leader_list

def dfs(graph, v, f, leader_list, visited, leader):
    """
    DFS algorithm on a given node v
    v: source node that DFS is called on
    f: a list of finishing time of each node, it will be modified in-place
    leader_list: a list of leader of each node, it will be modified in-place
    visited: a boolean list, it will be modified in-place
    """
    global time
    visited[v] = True
    leader_list[v] = leader
    for t in graph[v]:
        if not visited[t]:
            dfs(graph, t, f, leader_list, visited, leader)
    time += 1
    f[v] = time


if __name__ == '__main__':
    # read directed edges into a dictionary
    # nodes without outgoing edges will automatically be assigned empty list when they are accessed
    graph = defaultdict(list)
    graph_rev = defaultdict(list)
    n = 875714

    for line in open('scc.txt'):
        temp = line.split()
        temp = [int(i) for i in temp]
        graph[temp[0]].append(temp[1])
        graph_rev[temp[1]].append(temp[0])

    # first DFS-loop on reversed graph, get finishing time of each node
    time = 0
    f, _ = dfs_loop(graph_rev, n)
    # second DFS-loop on graph, get leader of each node
    time = 0
    _, leader = dfs_loop(graph, n, f)
    leader.pop(0)
    leader_count = Counter(leader)
    top_five = leader_count.most_common(5)
    out = open('result.txt', 'wt')
    print(top_five, file=out)
    out.close()
