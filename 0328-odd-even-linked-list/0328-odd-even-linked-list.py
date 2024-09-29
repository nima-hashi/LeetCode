# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        odd = ListNode()
        even = ListNode()
        
        curr = head
        oddCurr = odd
        evenCurr = even
        
        i = 1
        while curr:
            if i % 2 == 0:
                evenCurr.next = curr
                evenCurr = evenCurr.next
                
            if i % 2 == 1:
                oddCurr.next = curr
                oddCurr = oddCurr.next
                
            curr = curr.next
            i += 1
        
        evenCurr.next = None
        oddCurr.next = even.next
        
        return odd.next


            
        
        
            
        
        