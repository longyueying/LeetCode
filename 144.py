# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        rList = []
        stack = []
        currentNode = root
        while currentNode!=None or len(stack)!=0:
            if currentNode != None:
                rList.append(currentNode.val)
                stack.append(currentNode)
                currentNode = currentNode.left
            else:
                currentNode = stack.pop().right
        return rList

if __name__=="__main__":
    solution = Solution()
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6

    print(solution.preorderTraversal(node1))