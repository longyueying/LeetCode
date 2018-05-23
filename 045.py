class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = 0
        jump = 0
        while index < len(nums)-1:
            temp = index
            if index+nums[index] >= len(nums)-1:
                jump+=1
                return jump
            for i in range(index, index+nums[index]+1):
                if i + nums[i] > temp + nums[temp]:
                    temp = i
            index = temp
            jump +=1
        return jump

if __name__=="__main__":
    solu = Solution()
    jump = solu.jump([2,1])
    print(jump)