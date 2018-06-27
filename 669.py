# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if root==None:
            return
        elif root.val < L:
            root = root.right
            self.trimBST(root, L, R)
        elif root.val > R:
            root = root.left
            self.trimBST(root, L, R)
        else:
            self.trimBST(root.left, L, R)
            self.trimBST(root.right, L, R)
        return root
if __name__=="__main__":
    solu = Solution()
    a  = TreeNode(0)
    b = TreeNode(1)
    c = TreeNode(2)
    d = TreeNode(3)
    e = TreeNode(4)

    d.left = a
    d.right = e
    a.right = c
    c.left = b

    root = solu.trimBST(d, 1,3)

    print(root.val)
    print(root.left.val)
    print(root.right.val)