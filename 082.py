# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        h = ListNode(-1)
        h.next = head

        tmp = h
        while tmp.next!=None and tmp.next.next!=None:
            if tmp.next.val == tmp.next.next.val:
                v = tmp.next.val
                while tmp.next!= None and tmp.next.val == v:
                    tmp.next = tmp.next.next
            else:
                tmp = tmp.next
        return h.next


