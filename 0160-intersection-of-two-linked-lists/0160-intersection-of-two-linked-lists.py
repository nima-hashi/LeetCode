# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        cache = {}
        
        curr = headA
        
        while curr:
            if curr not in cache:
                cache[curr] = 1
                curr = curr.next
                
        curr = headB
        
        while curr:
            if curr not in cache:
                cache[curr] = 1
                curr = curr.next
            
            else: 
                return curr
            
        return None
        
        