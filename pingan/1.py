import sys
l = []

n = int(sys.stdin.readline().strip())
for i in range(n):
    line = sys.stdin.readline().strip()
    l.append(line)

def compare(a, b):
    tmp = a[0]
    len_a = len(a)
    len_b = len(b)
    for i in range(min(len_a,len_b)):
        if a[i] < b[i]:
            return -1
        elif a[i]>b[i]:
            return 1
    if len_a==len_b:
        return 0
    elif len_a>len_b:
        return -1
    else:
        return 1

for i in range(n):
    for j in range(n-i-1):
        c = compare(l[j], l[j+1])
        if c==1:
            tmp = l[j]
            l[j] = l[j+1]
            l[j+1] = tmp
print(''.join(l))