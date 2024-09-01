# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        ## fast and slow pointer to find mid m = fastSlow(head)
        ## rev m.next
        ## merge first half w second

        def revList(lst):

            if not lst:
                return lst
            
            prev = None
            curr = lst

            while curr:
                save = curr.next
                curr.next = prev
                prev = curr
                curr = save
            
            return prev

            

        if not head or not head.next:
            return head

        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        
        second_half = slow.next
        slow.next = None

        second_half = revList(second_half)

        # merge 

        dummy = ListNode(0)
        current = dummy

        while head and second_half:
            current.next = head
            head = head.next
            current = current.next

            current.next = second_half
            second_half = second_half.next
            current = current.next

        if head:
            current.next = head

        return  dummy.next