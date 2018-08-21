# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        pre = root
        while (pre.left!=None):
            cur = pre
            while cur != None:
                cur.left.next = cur.right
                if cur.next != None:
                    cur.right.next = cur.next.left
                cur = cur.next

