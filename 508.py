# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        self.sum = {}

        def treeSum(root):
            if root == None:
                return 0
            root.val = root.val+treeSum(root.left)+treeSum(root.right)
            self.sum.setdefault(root.val, 0)
            self.sum[root.val]+=1
            return root.val
        treeSum(root)

        print(self.sum)

        max = 0
        for k in self.sum:
            if self.sum[k]>max:
                max = self.sum[k]
        res = []
        for k in self.sum:
            if self.sum[k] == max:
                res.append(k)
        return res




