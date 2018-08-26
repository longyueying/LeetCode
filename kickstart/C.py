
class solution(object):
    def m(self, n, bala):
        self.res = []
        self.n = n
        self.sovler([], bala)
        return self.res

    def sovler(self,status, remain):
        if len(status)>= self.n:
            self.res.append((sum(status[:n]), sum(status[n:2*n]), sum(status[2*n:3*n])))
        for i, num in enumerate(remain):
            tnp = status[:]
            tnp.append(num)
            self.sovler(tnp, remain[:i]+remain[i+1:])

s = solution()
res = []
with open('input.in') as f:
    t = int(f.readline().strip())
    for i in range(t):
        print(i)
        n = int(f.readline().strip())
        bahu = list(map(int, f.readline().strip().split()))
        bala = list(map(int, f.readline().strip().split()))

        if sum(bala[:n]) >= sum(bahu[2*n:]):
            res.append(0)
        else:
            for j in (n, n + int(n/2)+1):
                tmp = bahu[j]
                bahu[j] = bahu[j+n]
                bahu[j+n] = tmp
            bahu1 = sum(bahu[:n])
            bahu2 = sum(bahu[n:2*n])
            bahu3 = sum(bahu[2*n:])
            if min(bahu2, bahu3) > sum(bala[2*n:]):
                res.append(1)
            else:
                com = s.m(n, bala)
                x = 0
                y = len(com)
                for bala1, bala2 , bala3 in com:
                    u = 0
                    if bala1 < bahu1:
                        u+=1
                    if bala2 < bahu2:
                        u+=1
                    if bala3 < bahu3:
                        u+=1
                    if u >=2:
                        x+=1
                res.append(x/y)


with open('anwer.out','w') as f:
    for i, c in enumerate(res):
        string = "Case #{}: {:.9f}\n".format(i+1, c)
        f.write(string)












