import sys
import math

id = 0


def dfs(node, ids, low, visiting, adj, ssc):
    visiting.append(node)

    global id
    id += 1
    ids[node] = id
    low[node] = id
    for child in adj[node]:
        if ids[child] == -1:
            dfs(child, ids, low, visiting, adj, ssc)
        if child in visiting:
            low[node] = min(low[node], low[child])

    if(low[node] == ids[node]):
        nodes = []
        while len(visiting):
            last = visiting.pop()
            nodes.append(last)
            if last != node:
                low[last] = low[node]
            if last == node:
                break
        ssc.append(nodes)


def number_of_strongly_connected_components(adj):
    result = 0
    ids = [-1]*len(adj)
    low = [-1]*len(adj)
    ssc = []

    # id = 0
    # write your code here
    for node in range(len(adj)):
        if ids[node] == -1:
            visiting = []
            dfs(node, ids, low, visiting, adj, ssc)

    # print(ids)
    # print(low)
    # print(ssc)
    result = len(ssc)

    return result


if __name__ == '__main__':
    input = input()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(number_of_strongly_connected_components(adj))
