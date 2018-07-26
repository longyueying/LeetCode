class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in len(nums):
            nums[abs(nums[i])] = -abs(nums[abs(nums[i])])
        for i in len(nums):
            if nums[i] < 0