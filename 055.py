class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        i=0
        while i < (len(nums)):
            nexti = i+nums[i]
            if nexti >= len(nums)-1:
                return True
            if nums[i] == 0:
                return False
            temp = nexti
            for j in range(i, temp+1):
                if j + nums[j]>temp:
                    temp = j + nums[j]
                    nexti = j
            i = nexti
        return True
if __name__=="__main__":
    solu = Solution()
    print(solu.canJump([3,0,8,2,0,0,1]))
