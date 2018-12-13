# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        t = head
        length = 0
        while head:
            length+=1
            head = head.next

        dummy = ListNode(0)
        dummy.next = t
        stepSize = 1
        while stepSize < length:
            cur =dummy.next
            tail = dummy
            while cur:
                left = cur
                right = self.split(left, stepSize)
                cur = self.split(right, stepSize)
                tail = self.merge(left, right, tail)
            stepSize = stepSize<<1
        return dummy.next

    def merge(self, left, right, tail):
        head = tail
        while left and right:
            if left.val < right.val:
                head.next = left
                head = head.next
                left = left.next
            else:
                head.next = right
                head = head.next
                right = right.next
        if left:
            head.next = left
        else:
            head.next = right
        while head.next:
            head = head.next
        return head

    def split(self, head, stepSize):
        i = 1
        while i<stepSize and head:
            head = head.next
            i+=1

        if not head:
            return None
        else:
            res = head.next
            head.next = None
            return res

if __name__=="__main__":
    a = ListNode(4)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(1)
    a.next = b
    b.next = c
    c.next = d

    s = Solution()
    r = s.sortList(a)
    while r:
        print(r.val)
        r = r.next