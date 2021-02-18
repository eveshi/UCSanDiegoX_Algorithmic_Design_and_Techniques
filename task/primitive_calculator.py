import sys
import math

def optimal_sequence(n):  
    d = {}
    d[1] = 0
    parent = [None]*(n+1)

    for i in range(2, n+1):
        curr_p = i - 1
        curr_val = d[i-1] + 1

        if i%2 == 0 and d[int(i/2)] + 1 < curr_val:
            curr_p = int(i/2)
            curr_val = d[int(i/2)] + 1
        
        if i%3 == 0 and d[int(i/3)] + 1 < curr_val:
            curr_p = int(i/3)
            curr_val = d[int(i/3)] + 1

        parent[i] = curr_p
        d[i] = curr_val
    
    sequence = [n]
    p = parent[n]
    while p:
        sequence.append(p)
        p = parent[p]
    
    return reversed(sequence)

if __name__ == '__main__':
    input = input()
    n = int(input)
    sequence = list(optimal_sequence(n))
    print(len(sequence) - 1)
    for x in sequence:
        print(x, end=' ')