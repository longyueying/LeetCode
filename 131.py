class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def isPali(s):
            i = 0
            j = len(s)-1

            while i < j:
                if s[i]!=s[j]:
                    return False
                i+=1
                j-=1
            return True

        self.res = []
        def solver(s,status, r):
            if not isPali(s):
                return
            if len(r)==0:
                self.res.append(status[:])
                return
            for i in range(1,len(r)+1):
                new = r[:i]
                tmp = status[:]
                tmp.append(new)
                solver(new, tmp,r[i:])
            return

        solver('', [], s)
        return self.res

if __name__=="__main__":
    s = Solution()
    print(s.partition('aab'))