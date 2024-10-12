# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        
        left, right = ListNode(), ListNode()
        l = left
        r = right
        
        curr = head
        
        while curr:
            if curr.val < x:
                l.next = curr
                l = l.next
                
            else:
                r.next = curr
                r =r.next
            
            curr = curr.next
        
        l.next = right.next
        r.next = None
        
        return left.next
                
        
        