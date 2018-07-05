# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        def solver(root):
            if root == None:
                return 0
            left_sum =solver(root.left)
            if left_sum == 0:
                root.left = None
            right_sum = solver(root.right)
            if right_sum == 0:
                root.right = None
            sum = root.val+left_sum+right_sum
            return sum
        solver(root)
        return root