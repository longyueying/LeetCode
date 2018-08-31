# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.updateNode(root)
        self.res = 0
        def solver(root):
            if root==None:
                return
            self.res+=(abs(self.getValue(root.left)-self.getValue(root.right)))
            solver(root.left)
            solver(root.right)
        solver(root)
        return self.res

    def getValue(self,node):
        if node==None:
            return 0
        else:
            return node.val

    def updateNode(self,root):
        if root==None:
            return 0
        root.val = root.val+self.updateNode(root.left)+self.updateNode(root.right)
        return root.val