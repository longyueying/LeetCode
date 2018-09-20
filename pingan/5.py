import sys

def compare(a, b):
    a = a.split('.')
    b = b.split('.')
    a_len = len(a)
    b_len = len(b)
    min_len = min(a_len, b_len)
    for i in range(min_len):
        if a[i]<b[i]:
            return -1
        elif a[i]>b[i]:
            return 1
    if a_len<b_len:
        return -1
    elif a_len>b_len:
        return 1
    else:
        return 0

n = int(sys.stdin.readline().strip())
l = []
for i in range(n):
    l.append(sys.stdin.readline().strip())

for i in range(n):
    for j in range(n-i-1):
        c = compare(l[j], l[j+1])
        if c==1:
            tmp = l[j]
            l[j] = l[j+1]
            l[j+1] = tmp
for i in range(n):
    print(l[i])