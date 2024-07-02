class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        count = {}
        
        for letter in s:
            if letter not in count:
                count[letter] = 1
            else:
                count[letter] += 1
                
        for letter in t:
            if letter not in count:
                return False
            
            count[letter] -= 1
            
            if count[letter] < 0:
                return False
            
        return max(count.values()) == 0
        
        
        
        
        