import sys
from collections import deque
grid = []
m = int(sys.stdin.readline().strip())
for i in range(m):
    line = sys.stdin.readline().strip().split()
    grid.append(line)
res = 0
if m == 0:
    print(0)
else:
    quene = deque()
    for i in range(m):
        for j in range(m):
            if grid[i][j]=='1':
                res+=1
                quene.append((i,j))
                while len(quene)>0:
                    k, q = quene.popleft()
                    if k>=0 and k < m and q >= 0 and q < m and grid[k][q]=='1':
                        grid[k][q]='0'
                        quene.extend([(k,q-1), (k,q+1),(k+1, q), (k-1,q)])
    print(res)