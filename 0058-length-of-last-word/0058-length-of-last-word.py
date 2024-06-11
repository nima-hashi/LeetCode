class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        prev = 0
        count = 0
        
        for elm in s:
            if elm == " ":
                if count != 0:
                    prev = count
                count = 0
                
            else:
                count += 1
                
        if s[-1] == " ":
            return prev
        return count
                
        
        