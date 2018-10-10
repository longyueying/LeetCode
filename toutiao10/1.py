import sys

def isValid(num,a,b):
    while num!=0:
        tmp = num%10
        if tmp!=a and tmp!=b:
            return False
        num = int(num/10)
    return True
def zuhe(i,k):
    t = 1
    if i==0 or i==k:
        return 1
    for i in range(k-i+1,k+1,1):
        t = t * i
    for i in range(1,i+1,1):
        t =int(t/i)
    return t

a, b, k = list(map(int, sys.stdin.readline().strip().split()))
res = 0
for i in range(k+1):
    num = i*a + (k-i)*b
    print(num)
    if isValid(num,a,b):
        res = res + zuhe(i,k)
print(res%1000000007)

