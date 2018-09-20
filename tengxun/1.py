import sys
k  = int(sys.stdin.readline().strip())
a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()
dic = {}
list_a = {}
for i in range(len(b)-k+1):
    dic.setdefault(b[i:i+k],0)
    dic[b[i:i+k]]+=1

res = 0
for i in range(len(a)-k+1):
    if a[i:i+k] in dic:
        if a[i:i+k] not in list_a:
            list_a[a[i:i+k]]=0
            res+=dic[a[i:i+k]]
print(res)