class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """

        h = ListNode(0)
        h.next = head
        i = 0
        tmp = h
        while i < m-1:
            tmp = tmp.next
            i+=1
        pos = tmp
        tmp = tmp.next
        i+=1
        while i <=n-1:
            nxt = tmp.next
            tmp.next = nxt.next
            nxt.next = pos.next
            pos.next = nxt
            i+=1
        return h.next



