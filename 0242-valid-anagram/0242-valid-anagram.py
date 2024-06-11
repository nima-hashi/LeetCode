class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        hashMap1 = {}
        hashMap2 = {}
        
        for elm in s:
            if elm not in hashMap1:
                hashMap1[elm] = 1
            
            else:
                hashMap1[elm] += 1
                
        for elm in t:
            if elm not in hashMap2:
                hashMap2[elm] = 1
            
            else:
                hashMap2[elm] += 1
        
        return hashMap1 == hashMap2
                
                
        
        
        