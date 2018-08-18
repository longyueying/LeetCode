class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        def sovler(status, index):
            res.append(status)

            while index < len(nums):
                tmp = nums[index]
                status.append(nums[index])
                sovler(status[:], index+1)
                status.pop()
                while index < len(nums) and nums[index] == tmp:
                    index+=1

        sovler([], 0)
        return res

if __name__=="__main__":
    s =Solution()
    print(s.subsetsWithDup([1,2,2]))

