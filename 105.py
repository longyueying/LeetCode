# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def solver(nums, preorder):
            if len(nums)==0:
                return None
            v = preorder.pop(0)
            t = TreeNode(v)
            pos = nums.index(v)
            t.left = solver(nums[:pos],preorder)
            t.right = solver(nums[pos+1:], preorder)
            return t
        return solver(inorder, preorder)
