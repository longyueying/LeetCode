import sys
a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()
len_a = len(a)
len_b = len(b)

dp =  [[0]*(len_b+1) for i in range(len_a+1)]

for i in range(len_a):
    for j in range(len_b):
        if a[i]==b[j]:
            dp[i+1][j+1] = dp[i][j]+1
        else:
            add = 0
            dp[i+1][j+1] = dp[i][j]
            if dp[i][j]<dp[i+1][j]:
               dp[i+1][j+1] = max(dp[i+1][j+1], dp[i+1][j])
            if dp[i][j]<dp[i][j+1]:
                dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j+1])
#时间复杂度是O(n^2)
print(dp[-1][-1])
