class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        begin = 0
        end = len(nums) - 1
        while end - begin > 1:
            mid = int((begin + end) / 2)
            if nums[begin] <= nums[mid] and nums[mid] <= nums[end]:
                return nums[begin]
            if nums[begin] < nums[mid]:
                begin = mid
            else:
                end = mid
        return min(nums[begin], nums[end])
