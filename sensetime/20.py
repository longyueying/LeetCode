import sys

m, n = list(map(int, sys.stdin.readline().strip().split()))

dp = [1]*(n+1)
if m < n:
    dp = [1] * (m)
    for i in range(1, m):
        dp[i] = sum(dp[:i])
else:
    dp = [1]*n
    for i in range(1, n):
        dp[i] = sum(dp[:i])
    for i in range(n,m):
        tmp = sum(dp)
        dp[:n-1] = dp[1:n]
        dp[n-1] = tmp

print(sum(dp)%10007)
