class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = [[]]

        def solver(status):
            if len(status)==0:
                for num in nums:
                    solver([num])
