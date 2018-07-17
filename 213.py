class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        elif len(nums)==1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0:2])
        elif len(nums) == 3:
            return max(nums[0:3])
        res = [[0]*(len(nums)) for i in range(2)]

        res[0][0] = nums[0]
        res[0][1] = max(nums[0], nums[1])

        res[1][1] = nums[1]
        res[1][2] = max(nums[1], nums[2])

        for i in range(2, len(nums)):
            res[0][i] = max(res[0][i-2]+nums[i], res[0][i-1])
        for i in range(3, len(nums)):
            res[1][i] = max(res[1][i - 2] + nums[i], res[1][i - 1])

        result = max(res[0][-2], res[1][-3]+nums[-1])
        return result

if __name__=="__main__":
    solu = Solution()
    print(solu.rob([1,7,9,2]))