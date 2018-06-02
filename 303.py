class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.sumlist = []
        if len(nums) > 0:
            self.sumlist.append(nums[0])
            for i in range(1, len(nums)):
                self.sumlist.append(nums[i]+self.sumlist[-1])

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.sumlist[j]
        else:
            return self.sumlist[j]- self.sumlist[i-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

if __name__=='__main__':
    solu  = NumArray([-2, 0, 3, -5, 2, -1])
    print(solu.sumRange(0,2))
