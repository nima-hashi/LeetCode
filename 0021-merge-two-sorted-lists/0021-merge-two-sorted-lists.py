# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, curr1, curr2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        new = ListNode()

        current = new
        # curr1 = list1
        # curr2 = list2

        while curr1 and curr2:
            if curr1.val <= curr2.val:
                current.next = curr1
                curr1 = curr1.next
            else:
                current.next = curr2
                curr2 = curr2.next

            current = current.next

        if curr1:
            current.next = curr1
        if curr2:
            current.next = curr2

        return new.next

