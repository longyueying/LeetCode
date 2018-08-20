class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        self.res = False
        self.solver(root,0,sum)
        return self.res



    def solver(self, root, v, sum):
        if self.res==True:
            return
        if root==None:
            return
        v = v + root.val
        if root.left==None and root.right==None:
            if v== sum:
                self.res=True
            return
        self.solver(root.left, v, sum)
        self.solver(root.right, v, sum)


