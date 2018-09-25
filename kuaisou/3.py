import sys
n,p,h,w = list(map(int,sys.stdin.readline().strip().split()))
a = list(map(int,sys.stdin.readline().strip().split()))
res = 1
while True:
    row_c = int(w/res)
    column_c = int(h/res)
    if row_c==0:
        res-=1
        break
    if column_c==0:
        res-=1
        break
    row_num = 0
    for i in range(n):
        if a[i]%row_c==0:
            row_num+=(int(a[i]/row_c))
        else:
            row_num += (int(a[i] / row_c)+1)

    if row_num%column_c==0:
        page_num = row_num/column_c
    else:
        page_num = row_num / column_c+1
    if page_num > p:
        res-=1
        break

    res+=1
print(res)
