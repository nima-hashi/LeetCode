# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
        
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        dummy = ListNode(0, head)
        
        # find the start of sublist that needs to be reversed
        
        prev, curr = dummy, dummy.next
        
        for i in range(left - 1):
            prev, curr = curr, curr.next
            
        # reverse the sublist
        
        p = None
        for i in range(right-left+1):
            save = curr.next
            curr.next = p
            p = curr
            curr = save
        
        
        
        # update pointers
        
        prev.next.next = curr
        prev.next = p
        
        return dummy.next
        
        