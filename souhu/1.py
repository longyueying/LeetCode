import sys

def solver():
    a,b = sys.stdin.readline().strip().split()
    if len(a)!=len(b):
        return 0
    l = []
    diff_a=[]
    diff_b=[]
    for i in range(len(a)):
        if a[i]!=b[i]:
            l.append(i)
            diff_a.append(a[i])
            diff_b.append(b[i])
    if len(l)==0:
        for i in range(len(a)-1):
            if a[i]==a[i+1]:
                return 1
        return 0
    if len(l)!=2:
        
        return 0
    if a[l[0]]==b[l[1]] and a[l[1]]==b[l[0]]:
        return 1
    else:
        return 0


print(solver())