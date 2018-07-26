class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(0, len(nums),2):
            if i == len(nums)-1 or nums[i]!=nums[i+1]:
                return nums[i]
if __name__=="__main__":
    solu = Solution()
    print(solu.singleNonDuplicate([1,1,2]))
