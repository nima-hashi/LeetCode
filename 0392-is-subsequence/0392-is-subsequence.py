class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        for elm in t:
            if not s:
                return True
            if elm == s[0]:
                s = s[1:]
            
                
        return s == ""
        