# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next
            if slow == fast:
                return True
        return False

        # s = []

        # curr = head
        # while curr and curr not in s:
        #     s.append(curr)
        #     curr = curr.next

        # if curr in s:
        #     return True
        # return False

        