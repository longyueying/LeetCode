import sys

class Solution(object):
    def main(self):
        n = int(sys.stdin.readline().strip())
        self.dic_a = {}
        self.dic_b = {}
        a = list(map(int, sys.stdin.readline().strip().split()))
        b = list(map(int, sys.stdin.readline().strip().split()))

        for i in range(n):
            self.dic_a[a[i]] = i+1
            self.dic_b[b[i]] = i + 1
        self.res = 0
        self.length = n
        self.solver(1, [])
        return self.res
    def solver(self, i, status):
        if i > self.length:
            if len(status)>self.res:
                self.res = len(status)
            return
        if self.length-i+1 + len(status) <=self.res:
            return

        flag = True
        for num in status:
            if self.dic_a[num] < self.dic_a[i] or self.dic_b[num] > self.dic_b[i]:
                flag = False
                break
        if flag==False:
            self.solver(i+1, status[:])
        else:
            tmp = status[:]
            tmp.append(i)
            self.solver(i + 1, tmp)
            self.solver(i + 1,status[:])


s = Solution()
print(s.main())