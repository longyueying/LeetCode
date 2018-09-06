class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        dic = {}
        degree = 1
        for i, num in enumerate(nums):
            if dic.__contains__(num):
                dic[num][0] += 1
                dic[num][2] = i
                if dic[num][0]>degree:
                    degree = dic[num][0]
            else:
                dic[num] = [1,i,i]
        res = len(nums)
        for k in dic:
            if dic[k][0]==degree:
                res = min(dic[k][2]-dic[k][1]+1, res)
        return res