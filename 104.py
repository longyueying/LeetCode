# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxdepth = 0
        def solver(root, depth):
            if root==None:
                return
            if depth > self.maxdepth:
                self.maxdepth=depth
            solver(root.left, depth+1)
            solver(root.right, depth+1)
        solver(root, 1)
        return self.maxdepth