import sys
str = sys.stdin.readline().strip()

str_len = len(str)

dp = [[1] * str_len for i in range(str_len)]

for i in range(str_len-1, -1, -1):
    for j in range(i+1, str_len):
        if j-i==1:
            if str[i]==str[j]:
                dp[i][j]=2
        else:
            if str[i] == str[j]:
                dp[i][j] = max(dp[i+1][j-1]+2, dp[i+1][j], dp[i][j-1])
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
res = 0
for line in dp:
    if max(line)>res:
        res = max(line)
print(res)