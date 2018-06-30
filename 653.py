# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    sorted_array = []
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        self.sorted_array = []
        self.solver(root)
        begin  = 0
        end = len(self.sorted_array) - 1
        while end > begin:
            sum = self.sorted_array[begin] + self.sorted_array[end]
            if sum == k:
                return True
            elif sum < k:
                begin+=1
            else:
                end-=1
        return False


    def solver(self, root):
        if root ==None:
            return
        self.solver(root.left)
        self.sorted_array.append(root.val)
        self.solver(root.right)

if __name__=="__main__":
    solu = Solution()
    a = TreeNode(5)
    b = TreeNode(3)
    c = TreeNode(6)
    d = TreeNode(2)
    e = TreeNode(4)
    f = TreeNode(7)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    solu.findTarget(a, 28)