class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for i in nums:
            if dic.__contains__(i):
                continue
            else:
                if dic.__contains__(i+1) and dic.__contains__(i-1):
                    dic[i] = dic[i-dic[i-1]] = dic[i+dic[i+1]] = dic[i-1]+dic[i+1]+1
                elif dic.__contains__(i+1):
                    dic[i] = dic[i+dic[i+1]] = dic[i+1]+1
                elif dic.__contains__(i-1):
                    dic[i] = dic[i - dic[i-1]] = dic[i - 1] + 1
                else:
                    dic[i] = 1
        return max(dic.values())