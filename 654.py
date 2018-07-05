# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) < 1:
            return None
        root = TreeNode(max(nums))

        def solver(root, nums, begin, end):
            if begin <= end:
                cur = nums.index(root.val)
                if begin < cur:
                    a = TreeNode(max(nums[begin:cur]))
                    root.left = a
                    solver(a, nums, begin, cur-1)
                if cur < end:
                    b = TreeNode(max(nums[cur+1:end+1]))
                    root.right = b
                    solver(b, nums, cur+1, end)
        solver(root, nums, 0, len(nums)-1)



