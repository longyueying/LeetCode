class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

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

if __name__=="__main__":
    s = Solution()
    print(s.restoreIpAddresses("010010"))