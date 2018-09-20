import sys
sys.setrecursionlimit(100000)
class solution(object):
    res = 0
    def run(self):
        n,k,w = list(map(int,sys.stdin.readline().strip().split()))
        self.solver(0,n,k,w,1)
        return self.res
    def solver(self,cur,n,k,w,prob):
        if cur>=k:
            if cur <=n:
                self.res= self.res + prob
            return
        for i in range(1,w+1,1):
            self.solver(cur+i,n,k,w,prob*(1/w))
s = solution()
result = s.run()
print(round(result,5))


