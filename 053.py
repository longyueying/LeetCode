class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = nums[0]
        max = temp
        for i in range(1, len(nums)):
            if temp < 0:
                temp = 0
            temp = temp + nums[i]
            if temp > max:
                max = temp
        return max

