import sys


def dfs(curr, adj, visiting, visited):
    if curr in visited:
        print(curr, visited, visiting)
        return False

    if curr in visiting:
        return True

    if not len(adj[curr]):
        return False

    for i in adj[curr]:
        if dfs(i, adj, visiting+[curr], visited):
            return True

    visited.append(curr)

    return False


def acyclic(adj):
    for j in range(len(adj)):
        visited = []
        if dfs(j, adj, [], visited):
            return 1

    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
