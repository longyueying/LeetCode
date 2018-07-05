# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    sum = 0
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.sum=0
        def solver(root):
            if root == None:
                return
            if (root.right):
                solver(root.right)
            self.sum+= root.val
            root.val = self.sum
            if (root.left):
                solver(root.left)
        solver(root)
        return root

if __name__ == "__main__":
    solu = Solution()
    a = TreeNode(2)
    b = TreeNode(0)
    c = TreeNode(3)
    d = TreeNode(-4)
    e = TreeNode(1)
    # f = TreeNode(7)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    # c.right = f
    solu.convertBST(a)
    print(a.val)
    print(b.val)
    print(c.val)
    print(d.val)
    print(e.val)
    # print(f.val)