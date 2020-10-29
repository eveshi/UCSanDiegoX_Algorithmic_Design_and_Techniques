import sys
import threading

def get_height(i, parents, height):
    if parents[i] == -1:
        return 1

    if i in height:
        return height[i]
    
    height[i] = get_height(parents[i], parents, height) + 1
    return height[i]


def compute_height(n, parents):
    # Replace this code with a faster implementation
    max_height = 0
    height = {}
    for vertex in range(n):
        current_height = get_height(vertex, parents, height)
        max_height = max(current_height, max_height)
    return max_height


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()