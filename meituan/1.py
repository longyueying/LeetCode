import sys

class Solution(object):
    path = {}
    res = 0
    def load(self):
        self.dic = {}
        self.n = int(sys.stdin.readline().strip())
        for i in range(self.n-1):
            begin,end = list(map(int,sys.stdin.readline().strip().split()))
            self.dic.setdefault(begin,[])
            self.dic[begin].append(end)
        return self.dic

    def solover(self,node):
        if not self.dic.__contains__(node):
            return 0
        sons = []
        for next in self.dic[node]:
            sons.append(1+self.solover(next))
        self.path[node] = sum(sons)
        return sum(sons)
    def final(self,node):
        if not self.dic.__contains__(node):
            return
        self.res-=1
        paths = []
        for next in self.dic[node]:
            paths.append(self.path[node])
        self.final(self.dic[node][paths.index(max(paths))])
    def run(self):
        self.load()
        self.res = (self.n-1)*2
        self.solover(1)
        self.final(1)
        return self.res
s = Solution()
print(s.run())