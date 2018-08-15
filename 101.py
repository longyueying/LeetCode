class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True

        def solver(p1, p2):
            if p1 == None and p2 == None:
                return True

            elif p1 == None or p2 == None:
                return False
            else:
                if p1.val == p2.val:
                    return solver(p1.left, p2.right) and solver(p2.left, p1.right)
                else:
                    return False

        res = solver(root.left, root.right)
        return res

if __name__ == "__main__":
    s = Solution()
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(3)
    e = TreeNode(2)

    a.left = b
    a.right = c
    b.left = d
    c.left = e

    print(s.isSymmetric(a))