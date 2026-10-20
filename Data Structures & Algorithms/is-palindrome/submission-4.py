import re

nonalpha_re = re.compile(r"[^a-z0-9]")

class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()
        i , j = 0, len(s) - 1
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while j > i and not s[j].isalnum():
                j -= 1
            
            if s[i] != s[j]:
                return False
        
            i += 1
            j -= 1

        return True
