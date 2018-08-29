class Solution(object):
    def begin(self, dimention):
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

    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        dimention = len(M)
        if dimention==0:
            return 0

        self.begin(dimention)
        for i in range(dimention):
            for j in range(dimention):
                if M[i][j]==1:
                    self.union(i, j)
        return self.count

if __name__=="__main__":
    M = [[1,1,0],[1,1,0],[0,0,1]]
    s = Solution()
    print(s.findCircleNum(M))

