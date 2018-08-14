# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        def solver(root1, root2):
            if root1==None and root2==None:
                return True
            elif root1==None and root2!=None:
                return False
            elif root1!= None and root2==None:
                return False
            else:
                if root1.val != root2.val:
                    return False
                else:
                    return solver(root1.left, root2.left) and solver(root1.right, root2.right)
        return solver(p,q)
