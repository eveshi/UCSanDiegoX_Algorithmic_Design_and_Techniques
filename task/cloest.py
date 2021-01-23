#Uses python3
import sys
import math

def minimum_distance(x, y):
    if len(x) < 2:
        return 0.0

    if len(x) == 2:
        return math.sqrt((x[0] - x[1])*(x[0] - x[1]) + (y[0] - y[1])*(y[0] - y[1]))

    #write your code here
    d = math.inf
    lo = min(x)
    hi = max(x)
    mid = (lo + hi) / 2

    l = 0
    r = len(x) - 1
    while l < r:
        if x[l] > mid:
            x[l], x[r] = x[r], x[l]
            y[l], y[r] = y[r], y[l]
            r -= 1
        else:
            l += 1

    mid_p = int((len(x) - 1)/2)
    left_d = math.inf
    right_d = math.inf
    for i in range(mid_p + 1):
        for j in range(i + 1, mid_p + 1):
            left_d = min(left_d, math.sqrt((x[i] - x[j])*(x[i] - x[j]) + (y[i] - y[j])*(y[i] - y[j])))

    for i in range(mid_p, len(x)):
        for j in range(i + 1, len(x)):
            right_d = min(right_d, math.sqrt((x[i] - x[j])*(x[i] - x[j]) + (y[i] - y[j])*(y[i] - y[j])))
    
    d = min(left_d, right_d)
    print(left_d, right_d)
    
    l = 0
    r = mid_p
    while l <= r:
        m = int((l+r)/2)
        if x[m] < mid - d:
            l = m + 1
        else:
            r = m - 1
    left_p = l

    l = mid_p + 1
    r = len(x) - 1
    while l <= r:
        m = int((l+r)/2)
        if x[m] <= mid + d:
            l = m + 1
        else:
            r = m - 1
    right_p = r

    for i in range(left_p, mid_p + 1):
        for j in range(mid_p+1, right_p + 1):
            print(d, i, j, math.sqrt((x[i] - x[j])*(x[i] - x[j]) + (y[i] - y[j])*(y[i] - y[j])))
            d = min(d, math.sqrt((x[i] - x[j])*(x[i] - x[j]) + (y[i] - y[j])*(y[i] - y[j])))

    return d

if __name__ == '__main__':
    input = input()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))