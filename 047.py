class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        if len(nums)==0:
            return []
        elif len(nums)==1:
            return [nums]
        else:
            self.permuteRec(nums, 0 , res)
        return  res
    def permuteRec(self, nums, begin, res):
        if begin == len(nums) - 1:
            res.append(nums[:])
            return

        for i in range(begin, len(nums)):
            if nums[begin:].index(nums[i])==i-begin:
                self.swap(nums, begin, i)
                self.permuteRec(nums, begin+1, res)
                self.swap(nums, begin, i)


    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp


if __name__=="__main__":
    solu = Solution()
    print(solu.permuteUnique([1,1,2]))