import sys
import itertools
import numpy

def partition3(A):
    s = sum(A)
    if s % 3 != 0 or len(A) < 3:
        return 0

    target = s // 3
    dp = [[0 for _ in range(target+1)] for _ in range(len(A)+1)]
    count = 0
    for i in range(1, len(A)+1):
        for j in range(1, target+1):
            dp[i][j] = dp[i-1][j]
            val = 0
            if A[i-1] <= j:
                val = dp[i-1][j-A[i-1]] + A[i-1]
            dp[i][j] = max(dp[i][j], val)
            if dp[i][j] == target:
                count += 1

    if count >= 3:
        return 1

    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))