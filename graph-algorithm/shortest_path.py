import sys
import queue
import math


def make_edge(adj, cost, graph):
    i = 0
    while i < len(adj):
        j = 0
        while j < len(adj[i]):
            graph.append((i, adj[i][j], cost[i][j]))
            j += 1
        i += 1


def shortet_paths(adj, cost, s, distance, reachable, shortest):
    # write your code here
    v = [math.inf]*len(adj)
    v[s] = 0
    graph = []
    make_edge(adj, cost, graph)
    i = 0
    while i < len(adj):
        for item in graph:
            u = item[0]
            x = item[1]
            w = item[2]
            # print(u, v[u], x, v[x], w)
            if v[u] != math.inf and v[u] + w < v[x]:
                v[x] = v[u] + w
        i += 1

    print(v)
    cir = queue.Queue()
    visited = set()
    i = 0
    for item in graph:
        u = item[0]
        x = item[1]
        w = item[2]
        if v[u] != math.inf and v[u] + w < v[x]:
            cir.put(x)
            visited.add(x)
            shortest[x] = 0

    while not cir.empty():
        curr = cir.get()
        for node in adj[curr]:
            if node not in visited:
                cir.put(node)
                visited.add(node)
                shortest[node] = 0

    i = 0
    while i < len(adj):
        if v[i] != math.inf:
            reachable[i] = 1
            distance[i] = v[i]
        i += 1


if __name__ == '__main__':
    # input = sys.stdin.read()
    # data = list(map(int, input.split()))
    # n, m = data[0:2]
    # data = data[2:]
    # edges = list(
    #     zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    # data = data[3 * m:]
    # adj = [[] for _ in range(n)]
    # cost = [[] for _ in range(n)]
    # for ((a, b), w) in edges:
    #     adj[a - 1].append(b - 1)
    #     cost[a - 1].append(w)
    # s = data[0]
    # s -= 1
    adj = [
        [1, 2],
        [2],
        [4],
        [2],
        [3],
        [0]
    ]
    cost = [
        [10, 100],
        [5],
        [7],
        [-18],
        [10],
        [-1]
    ]
    s = 0
    n = 6
    distance = [10**19] * n
    reachable = [0] * n
    shortest = [1] * n
    shortet_paths(adj, cost, s, distance, reachable, shortest)
    for x in range(n):
        if reachable[x] == 0:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(distance[x])
