class uninfind:
    def __init__(self, dimention):
        self.rootlist = list(range(dimention))
        self.sizelist = [[] for i in range(dimention)]

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