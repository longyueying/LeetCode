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
            return None

        root.left = self.trimBST(root.left, L, R)
        root.right = self.trimBST(root.right, L, R)

        if root.val < L:
            return root.right
        elif root.val > R:
            return root.left
        else:
            return root

if __name__=="__main__":
    solu = Solution()
    a  = TreeNode(0)
    b = TreeNode(1)
    c = TreeNode(2)
    d = TreeNode(3)
    e = TreeNode(4)

    # d.left = a
    # d.right = e
    # a.right = c
    # c.left = b
    b.left = a
    b.right = c
    res = solu.trimBST(b, 1,2)

    print(res.val)
    #print(res.left.val)
    print(res.right.val)