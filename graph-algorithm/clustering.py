import sys
import math
import heapq


def get_d(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)


def find_p(c, parents):
    p = c
    while parents[p] != p:
        p = parents[p]
    return p


def clustering(x, y, k):
    # write your code here
    # write your code here
    distance = []
    i = 0
    while i < len(x):
        j = i + 1
        while j < len(x):
            d = get_d(x[i], y[i], x[j], y[j])
            heapq.heappush(distance, (d, i, j))
            j += 1
        i += 1
    if k >= len(x):
        return d
    parents = [z for z in range(len(x))]
    c = len(x)
    while c > k:
        (shortest, s, e) = heapq.heappop(distance)
        p1 = find_p(s, parents)
        p2 = find_p(e, parents)
        # print(s, e, parents, p1, p2)
        if p1 == p2:
            continue
        parents[p2] = p1
        c -= 1
    p1 = p2 = -1
    while p1 == p2:
        if len(distance) == 0:
            return -1.
        (shortest, s, e) = heapq.heappop(distance)
        p1 = find_p(s, parents)
        p2 = find_p(e, parents)
    return shortest


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    print("{0:.9f}".format(clustering(x, y, k)))
