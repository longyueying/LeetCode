# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import sys
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        max_num = sys.maxsize
        while head:
            if head.val == max_num:
                return False
            head.val = max_num
            head = head.next
        return True