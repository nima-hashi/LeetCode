class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        stop = False
        count = 0
        
        for i in range(len(s) -1, -1, -1):
            if s[i] != " ":
                stop = True
                count += 1
            
            else:
                if stop:
                    return count
        return count
                
            
                
                
        
        