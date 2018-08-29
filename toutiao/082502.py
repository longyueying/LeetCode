import sys

n = int(sys.stdin.readline().strip())

class Solution(object):
    res = 0
    u = [1,2,3,4,5,6,7,8,9,0, '+','-','(',')']
    def isValid(self,arr):
        pass

    def sovler(self,chengshu,status,t):
        if chengshu==n:
            if self.isValid(status):
                self.res+=1
            return
        for c in self.u:
            self.sovler(chengshu+1,status[:].append(c),t)

    def run(self):
        s = Solution()
        s.sovler(0, [], n)
        print(self.res)

s =Solution()
s.run()

