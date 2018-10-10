import sys
n = int(sys.stdin.readline().strip())
dp = [0]*n
if n==1:
    print(2)
if n==2:
    print(3)
else:
    dp[0]=2
    dp[1] = 3
    for i in range(2,n):
        dp[i] = dp[i-1]+dp[i-2]
    print(dp[-1])