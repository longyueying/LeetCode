class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        length = len(nums)

        def solver(status, start):
            res.append(status)
            if start==length:
                return
            else:
                for i in range(start, length):
                    status.append(nums[i])
                    solver(status[:], i+1)
                    status.pop()
        solver([], 0)
        return res

if __name__=="__main__":
    s = Solution()
    print(s.subsets([1,2,3]))
