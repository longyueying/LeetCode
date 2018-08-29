class Solution(object):
    def load(self, dimention):
        self.rootlist = list(range(1, dimention+1))
        self.sizelist = [1]*dimention
        self.res=[]

    def find(self,element):
        if element!=self.rootlist[element-1]:
            self.rootlist[element-1] = self.find(self.rootlist[element-1])
        return self.rootlist[element-1]
    def union(self,a,b):
        roota = self.find(a)
        rootb = self.find(b)
        if roota==rootb:
            self.res = [a,b]
            return
        if self.sizelist[roota-1] < self.sizelist[rootb-1]:
            self.sizelist[rootb - 1]+=self.sizelist[roota-1]
            self.rootlist[roota-1] = rootb
        else:
            self.sizelist[roota - 1] += self.sizelist[rootb - 1]
            self.rootlist[rootb - 1] = roota

    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        nums = []
        for edge in edges:
            nums.extend(edge)
        dimention = max(nums)
        self.load(dimention)
        for a, b in edges:
            self.union(a,b)
        return self.res

