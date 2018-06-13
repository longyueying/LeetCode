class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        begin = 0
        end = len(nums)-1

        while begin < len(nums) and nums[begin]==0:
            begin+=1
        while end > -1 and nums[end] == 2:
            end-=1

        i = begin
        while i <= end:
            if nums[i]==2:
                self.swap(nums,i, end)
                end-=1
            elif nums[i] == 0:
                self.swap(nums,i, begin)
                begin+=1
                i+=1
            else:
                i+=1

    def swap(self, nums, a, b):
        temp = nums[a]
        nums[a] = nums[b]
        nums[b] = temp

if __name__=="__main__":
    solu = Solution()
    nums = [1,2,0]
    solu.sortColors(nums)
    print(nums)