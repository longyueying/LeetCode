# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def solver(root):
            if root==None:
                return 0
            left = solver(root.left)
            right = solver(root.right)

            if left == 0 or right==0:
                return 1+max(left,right)
            else:
                return min(left,right)+1
        return solver(root)