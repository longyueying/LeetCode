class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        def  solver(root):
            if root == None:
                return
            solver(root.left)
            solver(root.right)
            tmp = root.left
            root.left = root.right
            root.right = tmp

        solver(root)
        return root
