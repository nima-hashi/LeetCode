class Solution(object):
    def simplifyEmail(self, email):
        
        localName, domainName = email.split("@")
        removeLettersAfterPlus = localName.split("+")
        localName = removeLettersAfterPlus[0].replace(".", "")
        return localName+"@"+domainName
        
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        sent = []
        count = 0
        
        for email in emails:
            simplifiedEmail = self.simplifyEmail(email)
            if simplifiedEmail not in sent:
                sent.append(simplifiedEmail)
                count += 1
        return count
        
        