class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
    
        curMax = -1
        
        for i in range(len(arr) - 1, -1, -1):
            temp = arr[i]
            arr[i] = curMax
            
            curMax = max(curMax, temp)
            
        return arr


        