import sys
import queue


def distance(adj, s, t):
    # write your code here
    q = queue.Queue()
    q.put((s, 0))
    seen = set()
    seen.add(s)
    while not q.empty():
        (curr, length) = q.get()
        for node in adj[curr]:
            if node == t:
                return length + 1
            if node not in seen:
                q.put((node, length+1))
                seen.add(node)

    return -1


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
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
