import sys

num = int(sys.stdin.readline().strip())

l = []
i = 2
while i <= num:
    if num % i==0:
        l.append(str(i))
        num = num/i
    else:
        i+=1
print('*'.join(l))