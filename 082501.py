import sys

n = int(sys.stdin.readline().strip())
res = 0
if n==0:
    print(0)
dic = {}
for i in range(n):
    dic[i] = i
flag = True
value = []
for i in range(n):
    line = sys.stdin.readline().strip()
    line = list(map(int, line.split()))
    value.append(line)
while flag:
    flag = False
    for i in range(n):
        line = value[i]
        tmp = dic[i]
        for j in range(len(line) - 1):
            if dic[line[j]-1] < tmp:
                flag = True
                tmp = dic[line[j]-1]
        dic[i] = tmp
        for j in range(len(line)-1):
            dic[line[j]-1] = tmp
print(len(set(dic.values())))