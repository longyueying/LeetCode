#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    res = []
    temp = []
    def binaryTreePaths(self, root):
        self.res = []
        self.temp = []
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        self.inviteNode(root)
        return self.res
    def inviteNode(self, node):
        if node==None:
            return
        elif node.left == None and node.right == None:
            self.temp.append(node.val)
            t = []+self.temp
            self.res.append('->'.join(map(str, t)))
            self.temp.pop()
        else:

            self.temp.append(node.val)
            self.inviteNode(node.left)
            self.inviteNode(node.right)
            self.temp.pop()

if __name__=="__main__":
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(5)

    a.left = b
    a.right=c
    b.right = d
    solu = Solution()
    print(solu.binaryTreePaths(a))

