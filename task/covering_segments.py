import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def optimal_points(segments):
    points = []
    # write your code here
    segments = sorted(segments)
    prev = segments[0]

    for s in segments:
        curr = s
        if curr.start <= prev.end:
            prev = Segment(curr.start, min(prev.end, curr.end))
        else:
            points.append(prev.end)
            prev = curr

    points.append(prev.start)
    return points


if __name__ == '__main__':
    input = input()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(
        x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
