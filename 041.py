class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            while (nums[i] <= len(nums) and nums[i] > 0 and nums[i]!=i+1 and nums[nums[i] - 1]!=nums[i]):
                temp = nums[i]
                nums[i] = nums[temp - 1]
                nums[temp - 1] = temp
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1

        return len(nums)+1

if __name__ =='__main__':
    solu = Solution()
    print(solu.firstMissingPositive([2,2]))