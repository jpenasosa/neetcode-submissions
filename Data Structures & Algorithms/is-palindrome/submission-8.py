import re

pattern = re.compile(r"[^a-z0-9]")

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = pattern.sub("", s.lower())
        return s == s[::-1]