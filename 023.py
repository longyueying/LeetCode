# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return []
        if len(lists) == 1:
            return lists[0]
        return self.partition(lists)

    def partition(self, sublists):
        print(len(sublists))
        if len(sublists) == 1:
            return sublists[0]
        else:
            return self.merge(self.partition(sublists[0:int(len(sublists)/2)]), self.partition(sublists[int(len(sublists)/2): len(sublists)]))

    def merge(self, firstList, secondList):
        current = head = ListNode(0)

        while firstList != None and secondList != None:
            if firstList.val > secondList.val:
                current.next = secondList
                current = current.next
                secondList = secondList.next
            else:
                current.next = firstList
                current = current.next
                firstList = firstList.next
        if firstList != None:
            current.next = firstList
        else:
            current.next = secondList
        return head.next

if __name__ == "__main__":
    # lists = []
    # l1 = ListNode(1)
    # l2 = ListNode(0)
    # lists.append(l1)
    # lists.append(l2)
    #
    # solu = Solution()
    # l3 = solu.mergeKLists(lists)
    # while l3 != None:
    #     print(l3.val)
    #     l3 = l3.next
    head = l4 = ListNode(1)
    l4 = l4.next = ListNode(2)
    #l4 = l4.next
    while l4 != None:
        print(l4.val)
        l4 = l4.next




