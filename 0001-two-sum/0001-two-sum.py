class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        ind = {}
        
        for i, num in enumerate(nums):
            search = target - num
            if search in ind:
                return [ind[search], i]
            ind[num] = i
                
    