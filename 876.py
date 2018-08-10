# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        mid = head
        count = 1
        tmp = head
        while tmp != None:
            if count % 2 == 0:
                mid = mid.next
            count+=1
            tmp = tmp.next
        return mid