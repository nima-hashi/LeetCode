class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        hashMap = {}

        for i in range(len(nums)):
            search = target - nums[i]

            if search in hashMap:
                return [i, hashMap[search]]

            hashMap[nums[i]] = i





        