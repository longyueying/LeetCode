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
        while pre:
            head = None
            cur = pre
            pre = None
            while cur:
                if cur.left == None and cur.right==None:
                    cur = cur.next
                elif cur.left != None and cur.right != None:
                    if head != None:
                        head.next = cur.left
                    else:
                        pre = cur.left
                    cur.left.next = cur.right
                    head = cur.right
                    cur = cur.next
                elif cur.left !=None:
                    if head != None:
                        head.next = cur.left
                    else:
                        pre = cur.left
                    head = cur.left
                else:
                    if head != None:
                        head.next = cur.right
                    else:
                        pre = cur.right
                    head = cur.right