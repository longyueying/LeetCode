import sys
sys.setrecursionlimit(10000000)
class Solution(object):
    def load(self):
        self.res = 0
        self.m, self.n = list(map(int, sys.stdin.readline().strip().split()))

    def solver(self,remain):
        if remain==0:
            self.res+=1
            return
        i = 1
        while i<=self.n and i<=remain:
            self.solver(remain-i)
            i+=1
    def run(self):
        self.load()
        self.solver(self.m)
        return self.res

s = Solution()
print(s.run())
