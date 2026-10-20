import re

regex = re.compile(r"[^a-z0-9]")

class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = regex.sub("", s.lower())
        i , j = 0, len(s) - 1
        while i < j:            
            if s[i] != s[j]:
                return False
        
            i += 1
            j -= 1

        return True
