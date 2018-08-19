import sys
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.first = None
        self.second = None

        self.pre = TreeNode(-sys.maxsize-1)


        def traverse(root):
            if root ==None:
                return
            traverse(root.left)

            if (self.first == None and self.pre.val >= root.val):
                self.first = self.pre
            if (self.first != None and self.pre.val >= root.val):
                self.second = root

            self.pre = root
            traverse(root.right)

        traverse(root)
        tmp = self.first
        self.first =self.second
        self.second = tmp