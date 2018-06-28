class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = {}
        for num in nums:
            a.setdefault(num, 0)
            a[num]+=1
        for k in a.keys():
            if a[k] > int(len(nums)/2):
                return k

if __name__=="__main__":
    solu = Solution()
    print(solu.majorityElement([2,2,1,1,1,2,2]))