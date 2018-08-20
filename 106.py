class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder)==0:
            return None
        v = postorder.pop()
        t = TreeNode(v)

        pos = inorder.index(v)
        t.right = self.buildTree(inorder[pos+1:], postorder)
        t.left = self.buildTree(inorder[:pos], postorder)
        return t
