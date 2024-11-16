class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        intersect = []
        hashSet = set(nums1)
        
        for num in nums2:
            if num in hashSet:
                intersect.append(num)
                hashSet.remove(num)
        return intersect
        
        
        