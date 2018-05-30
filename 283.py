class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        num_zero = nums.count(0)
        for i in range(num_zero):
            nums.remove(0)
        for i in range(num_zero):
            nums.append(0)