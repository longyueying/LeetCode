class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        length = 0
        if len(nums)==0:
            return length
        for i in range(len(nums)):
            if nums[i] != val:
                nums[length] = val
                length+=1
        return nums[0:length]