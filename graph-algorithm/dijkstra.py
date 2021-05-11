import sys
import math
import heapdict


def distance(adj, cost, s, t):
    # write your code here
    d = {}
    d[s] = 0
    q = heapdict.heapdict()
    q[s] = 0
    seen = set()
    seen.add(s)
    while len(q):
        (curr, u) = q.popitem()
        i = 0
        while i < len(adj[curr]):
            node = adj[curr][i]
            dist = d.get(node, math.inf)
            dist_curr = cost[curr][i]
            if dist_curr + u < dist:
                d[node] = dist_curr + u
                q[node] = dist_curr + u
            seen.add(node)
            i += 1

    return d.get(t, -1)


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
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
