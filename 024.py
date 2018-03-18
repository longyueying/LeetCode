# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        i = 0
        current = ListNode(0)
        begin = current
        current.next = head
        re = head
        while current != None:
            if i % 2 == 0 and current.next != None and current.next.next != None:
                temp = current.next
                current.next = temp.next
                temp.next = current.next.next
                current.next.next = temp
            current = current.next
            i+=1
        return begin.next


if __name__ == "__main__":

    solu = Solution()
    l1 = ListNode(1)
    l2 = ListNode(2)
    l1.next = l2

    l3 = solu.swapPairs(l1)
    while l3 != None:
        print(l3.val)
        l3 = l3.next

