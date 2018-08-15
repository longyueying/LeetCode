class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.res = True
        def solver(begin, end, root):
            if self.res== False or root == None:
                return
            if begin == None and end ==None:
                solver(begin, root.val, root.left)
                solver(root.val, end, root.right)
            elif begin!=None and end != None:
                if root.val <=begin or root.val >= end:
                    self.res = False
                else:
                    solver(begin, min(root.val, end), root.left)
                    solver(max(root.val, begin), end, root.right)
            elif begin!=None:
                if root.val <=begin:
                    self.res = False
                else:
                    solver(begin, root.val, root.left)
                    solver(max(root.val, begin), end, root.right)
            else:
                if  root.val >= end:
                    self.res = False
                else:
                    solver(begin, min(root.val, end), root.left)
                    solver(root.val, end, root.right)
        solver(None, None,root)
        return self.res

