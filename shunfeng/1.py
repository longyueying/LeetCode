import sys
n = int(sys.stdin.readline().strip())
poly = list(map(float, sys.stdin.readline().strip().split(',')))
poly_x = []
for i in range(0,2*n,2):
    poly_x.append(poly[i])
poly_y = []
for i in range(1,2*n,2):
    poly_y.append(poly[i])
m = int(sys.stdin.readline().strip())
point = list(map(float, sys.stdin.readline().strip().split(',')))

point_x = []
for i in range(0,2*m,2):
    point_x.append(point[i])
point_y = []
for i in range(1,2*m,2):
    point_y.append(point[i])
rep = []
i=0
for i in range(n):
    x1 = poly_x[i]
    y1 = poly_y[i]
    x2 = poly_x[(i+1)%n]
    y2 = poly_y[(i + 1) % n]
    k = (y2-y1)/(x1-x2)
    b = y1-k*x1
    rep.append((k,b,x1,y1,x2,y2))

res = ''

for i in range(m):
    min_x = min(poly_x)
    max_x = max(poly_x)
    min_y = min(poly_y)
    max_y = max(poly_y)
    if not (point_x[i]<min_x or point_x[i] or point_y[i]<min_y or point_y[i]>max_y):
        accross = 0
        for k,b,x1,y1,x2,y2 in rep:
            if point_x[i] <= max(x1,x2) and point_x[i] >= min(x1,x2):
                if k*point_x[i]+b>=point_y[i]:
                    accross+=1
        if accross%2==1:
            res =res + "({},{})".format(point_x[i],point_y[i])
if res=='':
    print('No')
else:
    print(''.join(res))