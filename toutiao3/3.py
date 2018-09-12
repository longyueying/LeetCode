import sys
class Solution(object):
    def load(self):
        s = sys.stdin.readline().strip()
        return s
    def restoreIpAddresses(self, s):
        self.res = []
        def solver(status, s):
            if len(status) == 4:
                if len(s) == 0:
                    self.res.append(status[:])
            else:
                for i in range(3):
                    if i >= len(s):
                        break
                    elif i>0 and s[0]=='0':
                        continue
                    elif int(s[0:i+1])<=255:
                        status.append(s[0:i+1])
                        solver(status, s[i+1:])
                        status.pop()
        solver([], s)
        result = []
        for ip in self.res:
            result.append('.'.join(ip))
        return result

s = Solution()
str = s.load()
print(len(s.restoreIpAddresses(str)))