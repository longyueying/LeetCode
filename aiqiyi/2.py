# import sys
#
# n, m = list(map(int,sys.stdin.readline().strip().split()))
# a = list(map(int,sys.stdin.readline().strip().split()))
#
# max_h = max(a)
#
# begin = 0
# end = max_h
#
# def get(a, h):
#     s = 0
#     for i in range(len(a)):
#         sigle_get = a[i]-h
#         if sigle_get>0:
#             s+=sigle_get
#     return s
# res = 0
# while begin < end:
#     mid = int((begin+end)/2)
#     tmp = get(a,mid)
#     if tmp==m:
#         res = mid
#         break
#     elif tmp>m:
#         begin = mid+1
#         res = mid
#     else:
#         end = mid-1
# print(res)

import sys
n, m = list(map(int,sys.stdin.readline().strip().split()))
a = list(map(int,sys.stdin.readline().strip().split()))
max_h = max(a)
begin = 0
end = max_h

def get(a, h):
    s = 0
    for i in range(len(a)):
        sigle_get = a[i]-h
        if sigle_get>0:
            s+=sigle_get
    return s
res = 0
while begin < end:
    mid = int((begin+end)/2)
    tmp = get(a,mid)
    if tmp==m:
        res = mid
        break
    elif tmp>m:
        begin = mid+1
        if mid > res:
            res = mid
    else:
        end = mid-1
for i in range(res, max_h+1):
    if get(a,i)>=m:
        res = i
    else:
        break
print(res)