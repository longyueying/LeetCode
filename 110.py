class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.res = True

        def solver(root):
            if self.res == False or root==None:
                return 0
            if abs(solver(root.left)-solver(root.right)) > 1:
                self.res=False
                return 0
            return max(solver(root.left), solver(root.right))+1
        solver(root)

        return self.res