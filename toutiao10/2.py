import sys
class solver(object):
    def run(self):
        self.res = 0
        n = int(sys.stdin.readline().strip())
        m = int(sys.stdin.readline().strip())
        self.c = []
        for line in sys.stdin:
            a = line.split()
            if len(a)==0:
                break
            x = int(a[0])
            y = int(a[1])
            self.c.append([x,y])
        self.c.sort()
        self.lens = len(self.c)
        self.solve(0, n, m, 0)
        return self.res
    def solve(self, total, remain_n, remain_m, pos):
        if pos >= self.lens:
            if total>self.res:
                self.res = total
            return
        if remain_m<=0:
            if total>self.res:
                self.res = total
            return
        if self.c[pos][0] > remain_n:
            if total>self.res:
                self.res = total
            return
        self.solve(total+self.c[pos][1], remain_n-self.c[pos][0], remain_m-1, pos+1)
        self.solve(total, remain_n, remain_m, pos + 1)

s = solver()
print(s.run())