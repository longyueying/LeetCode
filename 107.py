# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        rList = []
        queneVal = []
        quene = []
        queneLevel = []
        currentindex = 0
        if root != None:
            quene.append(root)
        else:
            return rList
        queneLevel.append(0)

        while currentindex < len(quene):
            currentNode = quene[currentindex]
            queneVal.append(currentNode.val)
            if currentNode.left != None:
                quene.append(currentNode.left)
                queneLevel.append(queneLevel[currentindex]+1)
            if currentNode.right != None:
                quene.append(currentNode.right)
                queneLevel.append(queneLevel[currentindex] + 1)
            currentindex += 1
        #print(queneLevel)
        tmp = []
        for i in range(len(queneVal)-1, -1, -1):
            if i<(len(queneVal)-1) and queneLevel[i] < queneLevel[i+1]:
                rList.append(tmp)
                tmp = []
            tmp.append(queneVal[i])
        rList.append(tmp)

        for arr in rList:
            begin = 0
            end = len(arr)-1
            while begin < end:
                tmp = arr[begin]
                arr[begin] = arr[end]
                arr[end] = tmp
                begin+=1
                end-=1

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

    print(solution.levelOrder(node1))