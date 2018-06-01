# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head==None:
            return head
        length = 0
        secondend = head
        while secondend.next != None:
            length += 1
            secondend = secondend.next
        length += 1
        move = k % length
        if move == 0:
            return head

        firstend = head
        for i in range(1, length - move):
            firstend = firstend.next

        temp = firstend.next
        secondend.next = head
        firstend.next = None

        return temp

if __name__=='__main__':
    solu = Solution()
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    head = a
    k = 2
    h = solu.rotateRight(head, k)

    while h!=None:
        print(h.val)
        h = h.next


