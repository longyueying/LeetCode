import sys

n, m = list(map(int, sys.stdin.readline().strip().split()))
a = list(map(int, sys.stdin.readline().strip().split()))

q_num = int(sys.stdin.readline().strip())

for i in range(q_num):
    l, r = list(map(int, sys.stdin.readline().strip().split()))
    print(len(set(a[l-1:r])))

