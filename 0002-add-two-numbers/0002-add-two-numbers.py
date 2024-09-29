# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getAnsAndRem(self, num): 
        ans = num % 10
        rem = num // 10
        return ans, rem
    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        dum = ListNode()
        dummy = dum
        
        rem = 0
        
        while l1 and l2:
            ans, rem = self.getAnsAndRem(l1.val + l2.val + rem)
            dummy.next = ListNode(ans)
            dummy = dummy.next
            l1 = l1.next
            l2 = l2.next
            
        while l1:
            ans, rem = self.getAnsAndRem(l1.val+ rem)
            dummy.next = ListNode(ans)
            dummy = dummy.next
            l1 = l1.next
        
        while l2:
            ans, rem = self.getAnsAndRem(l2.val + rem)
            dummy.next = ListNode(ans)
            dummy = dummy.next
            l2 = l2.next
        
        if rem != 0:
             dummy.next = ListNode(rem)
            
        return dum.next
            
        
            
            
        