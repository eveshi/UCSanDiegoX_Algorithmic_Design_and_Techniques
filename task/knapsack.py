import sys

def optimal_weight(W, w):
    # write your code here
    dp = [[0]*(W+1) for _ in range(len(w)+1)]
    
    for i in range(1, len(w)+1):
        for j in range(1, W+1):
            val = 0
            if w[i-1] <= j:
                val = dp[i-1][j-w[i-1]] + w[i-1]
            dp[i][j] = max(dp[i-1][j], val)
    
    return dp[len(w)][W]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))