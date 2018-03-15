#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 != None and l2 != None:
            if l1.val > l2.val:
                head = l2
                l2 = l2.next
            else:
                head = l1
                l1 = l1.next
            end = head
        elif l1 == None and l2 != None:
            return l2
        elif l1 != None and l2 == None:
            return l1
        else:
            return None

        while l1 != None and l2 != None:
            if l1.val > l2.val:
                end.next = l2
                l2 = l2.next
            else:
                end.next = l1
                l1 = l1.next
            end = end.next
        if l1 != None:
            end.next = l1
        else:
            end.next = l2
        return head

if __name__=="__main__":
    end1 = l1 = ListNode(1)
    end2 = l2 = ListNode(1)

    end1.next = ListNode(2)
    end1 = end1.next

    end1.next = ListNode(4)
    end1 = end1.next

    end2.next = ListNode(3)
    end2 = end2.next

    end2.next = ListNode(4)
    end2 = end2.next

    solution = Solution()
    newlist = solution.mergeTwoLists(l1, l2)

    while newlist!=None:
        print(newlist.val)
        newlist = newlist.next