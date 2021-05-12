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


def minimum_distance(x, y):
    result = 0.
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
    parents = [z for z in range(len(x))]
    edges = 0
    while edges < len(x) - 1:
        (shortest, s, e) = heapq.heappop(distance)
        p1 = find_p(s, parents)
        p2 = find_p(e, parents)
        if p1 == p2:
            continue
        parents[p2] = p1
        edges += 1
        result += shortest
    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
