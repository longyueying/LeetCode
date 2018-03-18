# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def reverseKGroup(head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """
    dummy = ListNode(-1)
    dummy.next = head
    pre = dummy
    current = head
    length = 0

    while current != None:
        length += 1
        current = current.next
    current = head
    while (length >= k):
        for i in range(k - 1):
            temp = current.next
            current.next = temp.next
            temp.next = pre.next
            pre.next = temp
        pre = current
        current = pre.next
        length -= k
    return dummy.next

if __name__=="__main__":
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)

    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5

    li = reverseKGroup(l1, 2)
    while li != None:
        print(li.val)
        li = li.next