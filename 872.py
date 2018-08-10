class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """

        def leaf(root):
            res = []
            if root.left == None and root.right==None:
                res.append(root.val)
            else:
                if root.left != None:
                    res.extend(leaf(root.left))
                if root.right != None:
                    res.extend(leaf((root.right)))
            return res
        a = (leaf(root1))
        b = (leaf(root2))

        if len(a) !=len(b):
            return False
        else:
            for i in range(a):
                if a[i] != b[i]:
                    return False
        return True