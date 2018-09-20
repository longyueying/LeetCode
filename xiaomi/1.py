import sys

class solution(object):
    res = 0
    def run(self):
        n = int(sys.stdin.readline().strip())
        self.price = list(map(int, sys.stdin.readline().strip().split()))
        self.target = int(sys.stdin.readline().strip())
        self.length = len(self.price)
        self.solver(0, 0)
        print(self.res)


    def solver(self, pos, tmp_sum):
        if self.res==1:
            return
        if tmp_sum==self.target:
            self.res=1
            return
        if tmp_sum>self.target:
            return
        if pos >=self.length:
            return
        self.solver(pos+1, tmp_sum)
        self.solver(pos+1,tmp_sum+self.price[pos])
s = solution()
s.run()