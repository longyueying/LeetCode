import sys

class Solution(object):
    def load(self):
        self.res = 0
        self.n = int(sys.stdin.readline().strip())
        self.m = int(sys.stdin.readline().strip().split()[0])
        self.dic = {}
        for i in range(self.m):
            begin, end = map(int, sys.stdin.readline().strip().split())
            self.dic.setdefault(begin,[])
            self.dic[begin].append(end)
    def solver(self, node):
        self.res += 1
        if node == self.n-1:
            return
        if len(self.dic[node])==0:
            return
        for next in self.dic[node]:
            print(next)
            self.solver(next)


    def run(self):
        self.solver(0)
        return self.res

s = Solution()
s.load()
res = s.run()
print(res-1)

