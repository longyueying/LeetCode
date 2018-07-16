# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def output(self, node):
        res = []
        stack = [node]
        while len(stack)!=0:
            invite = stack.pop(0)
            if invite!=None:
                res.append(invite.val)
                stack.append(invite.left)
                stack.append(invite.right)
            else:
                res.append(None)
        return res

    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def clone(node):
            if node == None:
                return None
            root = TreeNode(node.val)
            root.left = clone(node.left)
            root.right = clone(node.right)
            return root

        if n < 1:
            return []
        res = [TreeNode(1)]
        for i in range(2, n+1):
            tmp = []
            for j in range(len(res)):
                oldroot = res[j]
                target = TreeNode(i)
                target.left = clone(oldroot)
                tmp.append(target)

                tmpold = oldroot
                while tmpold != None:
                    newNode = TreeNode(i)
                    newNode.left = tmpold.right
                    tmpold.right = newNode
                    target = clone(oldroot)
                    tmp.append(target)
                    tmpold.right = newNode.left
                    tmpold = tmpold.right
            res = tmp
        return res



if __name__=="__main__":
    solu = Solution()
    result = solu.generateTrees(3)
    for node in result:
        print(solu.output(node))



