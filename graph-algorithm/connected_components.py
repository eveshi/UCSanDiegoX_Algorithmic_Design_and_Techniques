import sys

visited = set()


def dfs(curr, adj):
    if curr in visited:
        return False

    visited.add(curr)

    for item in adj[curr]:
        dfs(item, adj)

    return True


def number_of_components(adj):
    result = 0
    for i in range(len(adj)):
        if dfs(i, adj):
            result += 1
    return result


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
    print(number_of_components(adj))
