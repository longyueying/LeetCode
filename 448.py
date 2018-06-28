class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for num in nums:
            nums[abs(num)-1] = -abs(nums[abs(num)-1])
        output = []
        for i in range(len(nums)):
            if nums[i]<0:
                output.append(i+1)
        return output

if __name__=="__main__":
    solu = Solution()
    print(solu.findDisappearedNumbers())