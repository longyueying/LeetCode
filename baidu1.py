import sys
n = int(sys.stdin.readline().strip())
l=[]
tmp = 0
for i in range(n):
    line = list(map(int, sys.stdin.readline().strip().split()))
    l.append((line[0],line[1]))


