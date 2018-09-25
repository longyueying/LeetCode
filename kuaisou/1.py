import sys
n = int(sys.stdin.readline().strip())
l = []
for i in range(n):
    line = sys.stdin.readline().strip()[-1:-7:-1]
    line = line[-1::-1]
    l.append(line)
l.sort()
for i in range(n):
    print(l[i])