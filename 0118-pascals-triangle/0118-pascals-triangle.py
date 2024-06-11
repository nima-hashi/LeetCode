class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        pascal = [[1]]
        count = 1
        
        while count < numRows:
            temp = [0] + pascal[-1] + [0]
            row = []
            
            for i in range(len(temp)-1):
                row.append(temp[i] + temp[i+1])
    
            pascal.append(row)
            count += 1
        
        return pascal
       