import sys

def solver():
    a,b = sys.stdin.readline().strip().split()
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
    if a_len<b_len and sum(a)<sum(b):
        return -1
    elif a_len>b_len and sum(a)>sum(b):
        return 1
    else:
        return 0
print(solver())