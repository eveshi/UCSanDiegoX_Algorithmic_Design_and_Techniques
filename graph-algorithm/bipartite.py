import sys
import queue


def bfs(adj, color, s):
    q = queue.Queue()
    q.put(s)
    color[s] = 0

    while not q.empty():
        curr = q.get()
        c = color[curr]
        for node in adj[curr]:
            if node == curr:
                return False
            if color[node] == c:
                return False
            if color[node] == -1:
                q.put(node)
                color[node] = 1-c

    return True


def bipartite(adj):
    # write your code here
    color = [-1]*len(adj)
    for node in color:
        if color[node] == -1:
            if not bfs(adj, color, node):
                return 0

    return 1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))
