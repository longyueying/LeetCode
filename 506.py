class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        nums_copy = nums[:]
        dic = {}
        nums_copy.sort(reverse=True)

        for i,num in enumerate(nums_copy):
            dic[num] = i+1

        res = []
        for num in nums:
            if dic[num] > 3:
                res.append(str(dic[num]))
            elif dic[num] == 1:
                res.append('Gold Medal')
            elif dic[num] == 2:
                res.append('Silver Medal')
            else:
                res.append('Bronze Medal')
        return res