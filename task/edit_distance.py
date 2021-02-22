# Uses python3
def edit_distance(s, t):
    #write your code here
    dp = [[0 for i in range(len(s)+1)] for j in range(len(t)+1)]
    for i in range(len(dp)):
        for j in range(len(dp[0])):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif t[i-1] == s[j-1]:
                dp[i][j] = min(dp[i-1][j-1], dp[i][j-1]+1, dp[i-1][j]+1)
            else:
                dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1

    return dp[len(t)][len(s)]

if __name__ == "__main__":
    print(edit_distance(input(), input()))