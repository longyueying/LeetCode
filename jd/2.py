import sys
class uninfind:
    def __init__(self, dimention):
        self.rootlist = list(range(dimention))
        self.sizelist = [1]*dimention
        self.count = dimention

    def find(self, element):
        if element!=self.rootlist[element]:
            self.rootlist[element] = self.find(self.rootlist[element])
        return self.rootlist[element]

    def union(self, a, b):
        roota = self.find(a)
        rootb = self.find(b)

        if roota==rootb:
            return
        if self.sizelist[roota] < self.sizelist[rootb]:
            self.sizelist[rootb]+=self.sizelist[roota]
            self.rootlist[roota] = rootb
        else:
            self.sizelist[roota] += self.sizelist[rootb]
            self.rootlist[rootb] = roota
        self.count-=1
res = []
t = int(sys.stdin.readline().strip())
for i in range(t):
    n, m = list(map(int,sys.stdin.readline().strip().split()))
    u = uninfind(n)
    for j in range(m):
        a,b = list(map(int,sys.stdin.readline().strip().split()))
        u.union(a-1,b-1)
    if u.count<=m+1:
        list.append('Yes')
    else:
        list.append('No')