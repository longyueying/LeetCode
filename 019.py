# Definition for singly-linked list.
class ListNode(object):
 def __init__(self, x):
     self.val = x
     self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        length = 0
        current = head
        while current != None:
            current = current.next
            length+=1
        index = length - n

        if index == 0:
            head = head.next
        else:
            current = head
            for i in range(index-1):
                current = current.next
            current.next = current.next.next
        return head