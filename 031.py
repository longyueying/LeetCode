class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        numsLen = len(nums)

        for i in range(numsLen-1, -1, -1):
            if i<=0:
                self.reverseNums(nums, 0, numsLen-1)
            if nums[i-1] < nums[i]:
                self.reverseNums(nums, i , numsLen-1)
                for j in range(i, numsLen):
                    if nums[i-1] < nums[j]:
                        self.swapNums(nums, i-1, j)
                        return

    def swapNums(self, nums, firstIndex, secondIndex):
        tmp = nums[firstIndex]
        nums[firstIndex] = nums[secondIndex]
        nums[secondIndex] = tmp

    def reverseNums(self, nums, start, end):
        if start >= end:
            return
        else:
            for i in range(start, int((start+end+1)/2)):
                self.swapNums(nums, i, start+end-i)

if __name__ == '__main__':
    solution = Solution()
    nums = [1,1]
    solution.nextPermutation(nums)
    print(nums)