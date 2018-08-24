# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        lenA = 0
        lenB = 0
        cur = headA
        while cur!=None:
            lenA+=1
            cur = cur.next
        cur = headB
        while cur!=None:
            lenB+=1
            cur = cur.next
        if lenA==0 or lenB==0:
            return None

        curA = headA
        curB = headB

        if lenA > lenB:
            i = 0
            while i < lenA-lenB:
                i+=1
                curA = curA.next
        elif lenA < lenB:
            i = 0
            while i < lenB - lenA:
                i+=1
                curB = curB.next
        while curA!=None:
            if curA == curB:
                return curA
            else:
                curA = curA.next
                curB = curB.next
        return None
