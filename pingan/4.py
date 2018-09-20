import sys

year = int(sys.stdin.readline().strip())
month = int(sys.stdin.readline().strip())
day = int(sys.stdin.readline().strip())
dic = {1:31, 2:28, 3:31, 4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

if year%4==0 and year%100!=0:
    dic[2]=29
res = 0
for i in range(1,month):
    res+=dic[i]
res+=day
print(res)