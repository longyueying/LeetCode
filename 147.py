# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        node = ListNode(0)
        node.next = head

        cur = head.next
        cur_pre = head
        while cur:
            pre = node
            next = cur.next
            flag = True
            while pre.next != cur:
                if pre.next.val > cur.val:
                    flag = False
                    cur_pre.next = cur.next
                    cur.next = pre.next
                    pre.next = cur
                    break
                pre = pre.next
            cur = next
            if flag==True:
                cur_pre = cur_pre.next
        return node.next

