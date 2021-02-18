import sys
import math

def get_change(m):
    #write your code here
    coins = [1, 3, 4]
    l = [math.inf]*(m+1)
    l[0] = 0
    i = 0
    while i < m+1:
        for c in coins:
            if i - c >= 0:
                l[i] = min(l[i], l[i - c] + 1)
        i += 1

    return l[m]

if __name__ == '__main__':
    input = input()
    m = int(input)
    print(get_change(m))
