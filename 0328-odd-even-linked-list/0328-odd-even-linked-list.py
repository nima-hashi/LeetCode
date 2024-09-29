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
        
        if not head or not head.next or not head.next.next:
            return head
        
        oddPtr = curr = head
        evenPtr = evenHead = head.next
        
        c = 1
        
        while curr:
            if c > 2 and c % 2 == 1:
                oddPtr.next = curr
                oddPtr = oddPtr.next
                
            if c > 2 and c % 2 == 0:
                evenPtr.next = curr
                evenPtr = evenPtr.next
            
            curr = curr.next
            c += 1
            
        evenPtr.next = None 
        oddPtr.next = evenHead
        
        return head
            
        
        
#         odd = ListNode()
#         even = ListNode()
        
#         curr = head
#         oddCurr = odd
#         evenCurr = even
        
#         i = 1
#         while curr:
#             if i % 2 == 0:
#                 evenCurr.next = curr
#                 evenCurr = evenCurr.next
                
#             if i % 2 == 1:
#                 oddCurr.next = curr
#                 oddCurr = oddCurr.next
                
#             curr = curr.next
#             i += 1
        
#         evenCurr.next = None
#         oddCurr.next = even.next
        
#         return odd.next


            
        
        
            
        
        