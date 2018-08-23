class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        t2 = ListNode(0)

        length = 0

        cur = head
        while cur != None:
            length += 1
            cur = cur.next
        if length < 3:
            return
        mid = int(length / 2)
        i = 0
        cur = head
        while i < mid:
            cur = cur.next
            i += 1
        tmp = cur.next
        cur.next = None
        cur = tmp

        t2.next = cur
        while cur.next != None:
            tmp = cur.next
            cur.next = tmp.next
            tmp.next = t2.next
            t2.next = tmp
        t2 = t2.next
        cur = head
        while t2 != None:
            tmp = t2.next
            t2.next = cur.next
            cur.next = t2
            t2 = tmp
            cur = cur.next.next