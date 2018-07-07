# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1==None:
            return t2
        if t2 == None:
            return t1
        def solver(r1, r2):
            r1.val = r1.val+r2.val
            if r1.left == None and r2.left!=None:
                r1.left = r2.left
            elif r1.left!=None and r2.left!=None:
                solver(r1.left, r2.left)

            if r1.right == None and r2.right!=None:
                r1.right = r2.right
            elif r1.right!=None and r2.right!=None:
                solver(r1.right, r2.right)
        solver(t1, t2)
        return t1


