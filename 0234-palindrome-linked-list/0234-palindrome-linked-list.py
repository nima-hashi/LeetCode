# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        # flip head
        def reverse(head):
            prev = None
            curr = head
            nextt = head

            while curr is not None:
                nextt = nextt.next
                curr.next = prev
                prev = curr
                curr = nextt
            
            return prev

        # compare flipped w original
        
        def copyList(head):
            
            new = ListNode()
            tmp = new
            
            while head and new:
                new.next = ListNode(head.val)
                head = head.next
                new = new.next
            
            return tmp.next
        
        # compare flipped w original    
            
        copy = copyList(head)
        
        head2 = reverse(copy)

        while head:
            if head.val != head2.val:
                return False

            head = head.next
            head2 = head2.next

        return True
        