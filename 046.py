class Solution(object):
    result = []
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.result = []
        if len(nums)== 0:
            return []

        if len(nums) == 1:
            return [nums]
        self.permuteRecusive(nums,0)
        return self.result

    def permuteRecusive(self, nums, begin):

        if begin >= len(nums) -1:
            self.result.append(nums[:])
        else:
            for i in range(begin, len(nums)):
                temp = nums[begin]
                nums[begin] = nums[i]
                nums[i] = temp

                self.permuteRecusive(nums, begin+1)
                temp = nums[begin]
                nums[begin] = nums[i]
                nums[i] = temp

if __name__=="__main__":
    solu = Solution()
    print(solu.permute([1,2,3]))