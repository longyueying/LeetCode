# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = root.val
        def solver(root):
            if root == None:
                return 0
            sum_l = root.val+solver(root.left)
            sum_r = root.val+solver(root.right)
            total = sum_l + sum_r - root.val
            if max(sum_l,sum_r, total) > self.res:
                self.res = max(sum_l, sum_r, total)
            return max([sum_r, sum_l, 0])
        solver(root)
        return self.res

