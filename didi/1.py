import sys

class solution(object):
    res = 0
    def run(self):
        l = list(map(int, sys.stdin.readline().strip().split()))
        if max(l)-1 > sum(l)-max(l):
            return 0
        elif max(l)==2 and min(l)==1 and sum(l)==4:
            return 6
        else:
            self.solve(l, -1)
            return self.res

    def solve(self,l, head):
        if sum(l)==0:
            self.res+=1
            return
        if max(l)-1 > sum(l)-max(l):
            return
        for i in range(3):
            if i != head and l[i]>0:
                tmp = l[:]
                tmp[i]-=1
                self.solve(tmp,i)
s = solution()
print(s.run())