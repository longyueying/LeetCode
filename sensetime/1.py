import sys

N = int(sys.stdin.readline().strip())
l = []
n = 0
for i in range(N):
    q, u = list(map(float, sys.stdin.readline().strip().split()))
    n+=q
    l.append([u,q])
l.sort(reverse=True)
i = 0
total = 0
if n==0:
    print(100)
    print(100)
    print(100)
    print(100)
    print(100)
    print(100)
    print(100)
else:
    while total < 0.3*n:
        total+=l[i][1]
        i+=1
    res = int((total/(i))*100)
    print(res)
    while total < 0.4*n:
        total+=l[i][1]
        i+=1
    res = int((total/(i))*100)
    print(res)
    while total < 0.5*n:
        total+=l[i][1]
        i+=1
    res = int((total/(i))*100)
    print(res)
    while total < 0.6*n:
        total+=l[i][1]
        i+=1
    res = int((total/(i))*100)
    print(res)
    while total < 0.7*n:
        total+=l[i][1]
        i+=1
    res = int((total/(i))*100)
    print(res)
    while total < 0.8*n:
        total+=l[i][1]
        i+=1
    res = int((total/(i))*100)
    print(res)
    while total < 0.9*n:
        total+=l[i][1]
        i+=1
    res = int((total/(i))*100)
    print(res)