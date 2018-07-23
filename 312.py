class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + nums + [1]
        len_arr = len(nums)
        res = [[0] * len_arr for i in range(len_arr)]

        for i in range(2, len_arr):
            for left in range(0, len_arr-i):
                right  = left+i
                for k in range(left+1, right):
                    res[left][right] = max(res[left][right], nums[left]*nums[k]*nums[right]+res[left][k]+ res[k][right])
        return res[0][len_arr-1]