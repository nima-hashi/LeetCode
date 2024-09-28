# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def splitLinkedListInHalf(self, head):
        left = head
        right = head.next

        while right and right.next:
            left = left.next
            right = right.next.next

        right = left.next
        left.next = None
        return [head, right]

    def mergeLinkedList(self, L1, L2):

        dummy = ListNode()
        finalCurr = dummy
        curr1, curr2 = L1, L2

        while curr1 and curr2:
            if curr1.val <= curr2.val:
                finalCurr.next= curr1
                curr1 = curr1.next
            
            else:
                finalCurr.next = curr2
                curr2 = curr2.next

            finalCurr = finalCurr.next
        
        if curr1:
            finalCurr.next = curr1
        
        else:
            finalCurr.next = curr2

        return dummy.next


    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head or not head.next:
            return head
        
        halves = self.splitLinkedListInHalf(head)
        first, second = halves[0], halves[1]
        leftSide = self.sortList(first)
        rightSide = self.sortList(second)

        return self.mergeLinkedList(leftSide, rightSide)


        
        