class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if len(s) != len(t):
            return False
        
        count = Counter(s)
        
        for letter in t:
            if letter not in count or count[letter] == 0:
                return False
            count[letter] -= 1
            
        return True
            
        
        
        
        
        
        