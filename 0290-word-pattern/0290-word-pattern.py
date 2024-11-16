class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        
        charToWord = {}
        wordToChar = {}
        words = s.split()
        
        if len(words) != len(pattern):
            return False
        
        for i in range(len(pattern)):
            if pattern[i] in charToWord and charToWord[pattern[i]] != words[i]:
                return False
            if words[i] in wordToChar and wordToChar[words[i]] != pattern[i]:
                return False
            charToWord[pattern[i]] = words[i]
            wordToChar[words[i]] = pattern[i]
        
        return True
        
        