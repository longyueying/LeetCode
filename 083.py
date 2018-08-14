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
        if head == None:
            return head
        tmp = head
        while tmp.next!=None:
            if tmp.next.val == tmp.val:
                tmp.next = tmp.next.next
            else:
                tmp = tmp.next
        return head