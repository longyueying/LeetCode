import sys

res = 0
s = sys.stdin.readline().strip()

dic = {}
left = 0
right = 0

for right in range(len(s)):
    dic.setdefault(s[right],0)
    dic[s[right]]+=1
    while dic[s[right]]>1:
        dic[s[left]]-=1
        left+=1
    if right-left+1>res:
        res = right-left+1
print(res)