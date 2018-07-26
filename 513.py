# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.deepest = 1
        self.res = root.val

        def solver(root, deepth):
            if root == None:
                return
            if deepth >= self.deepest:
                if root.left != None:
                    self.deepest = deepth+1
                    self.res = root.left.val
            if deepth >= self.deepest:
                if root.right != None:
                    self.deepest = deepth+1
                    self.res = root.right.val
            solver(root.left, deepth+1)
            solver(root.right, deepth+1)
        solver(root, 1)
        return self.res
