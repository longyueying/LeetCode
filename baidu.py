import sys
n = int(sys.stdin.readline().strip())
a = list(map(int, sys.stdin.readline().strip().split()))

dp = [0]*n
for j in range(1,n):
    tmp = 0
    for i in range(j):
        if a[i]>a[j]:
            tmp+=1
    dp[j] = dp[j-1]+tmp

res = dp[-1]
pos = 0

for i in range(n):
    change = 0
    for p in range(i):
        if a[p] <= a[i]:
            change+=1
    for q in range(i+1,n):
        if a[q] < a[i]:
            change-=1
    tmp = dp[-1]+change
    if tmp < res:
        res = tmp
        pos = i
print(res, pos+1)