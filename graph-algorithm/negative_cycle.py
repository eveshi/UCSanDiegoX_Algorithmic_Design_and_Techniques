import sys
import math


def check_neg(graph, s, v):
    i = s
    while i < len(adj):
        for item in graph:
            u = item[0]
            x = item[1]
            w = item[2]
            print(u, v[u], x, v[x], w)
            if v[u] + w < v[x]:
                v[x] = v[u] + w
        i += 1
    i = s
    print(v)
    for item in graph:
        u = item[0]
        x = item[1]
        w = item[2]
        if v[u] + w < v[x]:
            return True
    return False


def make_edge(adj, cost, graph):
    i = 0
    while i < len(adj):
        j = 0
        while j < len(adj[i]):
            graph.append((i, adj[i][j], cost[i][j]))
            j += 1
        i += 1


def negative_cycle(adj, cost):
    # write your code here
    v = [math.inf]*len(adj)
    graph = []
    make_edge(adj, cost, graph)
    i = 0
    while i < len(adj):
        if v[i] == math.inf:
            v[i] = 0
            if check_neg(graph, i, v):
                return 1
        i += 1
    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(
        zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))
