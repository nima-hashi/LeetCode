# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    
    def splitListToParts(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        # Step 1: Calculate the total length of the list
        length, curr = 0, head
        while curr:
            curr = curr.next
            length += 1

        # Step 2: Determine the size of each part
        sublistLen, rem = length // k, length % k

        # Step 3: Initialize the result list
        res = []
        curr = head
        
        # Step 4: Split the list into parts
        for i in range(k):
            res.append(curr)  # Add the start of the current part
            
            # Move `curr` forward by `sublistLen + (1 if rem > 0 else 0)` nodes
            prev = None
            for j in range(sublistLen + (1 if rem > 0 else 0)):
                if curr:
                    prev = curr
                    curr = curr.next
            
            # Decrement rem if we added an extra node to this part
            if rem > 0:
                rem -= 1
            
            # If prev is not None, set its `next` to None to break the list
            if prev:
                prev.next = None
        
        # If there are fewer nodes than k, append `None` to the result list
        while len(res) < k:
            res.append(None)
        
        return res
