class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.res = []
        nums = []
        self.solver(root, nums, 0, sum)
        return self.res
    def solver(self, root, nums, v, sum):
        if root==None:
            return

        nums.append[root.val]
        v = v + root.val
        if root.left==None and root.right==None:
            if v== sum:
                self.res.append(nums[:])
            nums.pop()
            return
        self.solver(root.left, nums, v, sum)
        self.solver(root.right, nums, v, sum)
        nums.pop()