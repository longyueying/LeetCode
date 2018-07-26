class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.res = []

        def solver(root, deepth):
            if root == None:
                return
            if deepth+1 > len(self.res):
                self.res.append(root.val)
            elif self.res[deepth] < root.val:
                self.res[deepth] = root.val
            solver(root.left, deepth+1)
            solver(root.right, deepth+1)

        solver(root, 0)
        return self.res



