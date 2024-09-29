# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getLen(self, node):
        
        c = 0
        curr = node
        while curr:
            c += 1
            curr = curr.next
        return c
    
    def findStartOfPath(self, node, move):
        
        curr = node
        while curr and move != 0:
            curr = curr.next
            move -= 1
        
        return curr
    
    def intersection(self, startA, startB):
        
        while startA and startB:
            if startA == startB:
                return startA
            startA = startA.next
            startB = startB.next
        return None    
        
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        c1 = self.getLen(headA)
        c2 = self.getLen(headB)
        
        pathLen = min(c1, c2)
        
        if c1 > pathLen:
            move = c1 - pathLen
            startA = self.findStartOfPath(headA, move)
        
        else:
            startA = headA
            
        if c2 > pathLen:
            move = c2 - pathLen
            startB = self.findStartOfPath(headB, move)
            
        else:
            startB = headB
        
        return self.intersection(startA, startB)
        
        
        
        
        
#         cache = {}
        
#         curr = headA
        
#         while curr:
#             if curr not in cache:
#                 cache[curr] = 1
#                 curr = curr.next
                
#         curr = headB
        
#         while curr:
#             if curr not in cache:
#                 cache[curr] = 1
#                 curr = curr.next
            
#             else: 
#                 return curr
            
#         return None
        
        