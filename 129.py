# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0

        def solver(root, path):
            if root.left==None and root.right==None:
                self.res = path*10 + root.val + self.res
                return
            if root == None:
                return

            solver(root.left, path*10+root.val)
            solver(root.right, path*10+root.val)
            return
        solver(root, 0)
        return self.res