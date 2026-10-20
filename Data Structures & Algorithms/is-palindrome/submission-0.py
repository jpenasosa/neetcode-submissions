import re

nonalpha_re = re.compile(r"[^a-z0-9]")

class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = nonalpha_re.sub("", s.lower())
        return string[::-1] == string