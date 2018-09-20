import sys
a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()
len_a = len(a)
len_b = len(b)

dic = {}
for i in range(len(a)):
    dic.setdefault(a[i],0)
    dic[a[i]]+=1
for i in range(len(b)):
    if b[i] in dic:
        dic[b[i]]-=1
print(len_a-sum(dic.values()))