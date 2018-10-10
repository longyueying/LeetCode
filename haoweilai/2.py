import sys
l, r = list(map(int, sys.stdin.readline().strip().split()))
res = 0
arr_l = list(str(l))
arr_r = list(str(r))
len_l = len(l)
len_r = len(r)

if len_l==len_r:
    for i in range(l,r+1,1):


print(res)