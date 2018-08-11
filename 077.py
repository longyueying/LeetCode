class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.res = []

        nums = [i for i in range(1, n+1)]

        def solver(status):
            if len(status) >= k:
                self.res.append(status)
                return
            if len(status)==0:
                for num in nums:
                    solver([num])
            else:
                for num in range(status[-1]+1, n+1):
                    solver(status+[num])
        solver([])
        return self.res

if __name__=="__main__":
    s = Solution()
    print(s.combine(4,2))

