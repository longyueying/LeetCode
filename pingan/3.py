import sys
l = []
for i in range(3):
    l.append(int(sys.stdin.readline().strip()))
l.sort()
print(l)