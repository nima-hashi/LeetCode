class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        hashMap = {}
        
        for num in nums:
            if str(num) not in hashMap:
                hashMap[str(num)] = 1
            else:
                hashMap[str(num)] += 1
        
        return max(hashMap.values()) > 1
                