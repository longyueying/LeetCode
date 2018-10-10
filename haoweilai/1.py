import sys
k,b,n,t = list(map(int, sys.stdin.readline().strip().split()))

total = 1
for i in range(n):
    total = k*total+b

res = n
tmp = t
if t>= total:
    print(0)
else:
    for i in range(n):
        tmp = k*tmp+b
        if tmp>=total:
            res = i+1
            break
    print(res)