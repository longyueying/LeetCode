class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        def solver(nums):
            if len(nums) == 0:
                return None
            if len(nums)==1:
                return TreeNode(nums[0])
            mid = int(len(nums)/2)
            t = TreeNode(nums[mid])
            t.left = solver(nums[:mid])
            t.right = solver(nums[mid+1:])
            return t
        return solver(nums)


