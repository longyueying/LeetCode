class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 1
        for i in range(len(nums)):
            while (nums[i] <= len(nums) and nums[i] > 0 and nums[i]!=i+1):
                temp = nums[i]
                nums[i] = nums[temp - 1]
                nums[temp - 1] = temp
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1

        return len(nums)

if __name__ =='__main__':
    solu = Solution()
    print(solu.firstMissingPositive([]))