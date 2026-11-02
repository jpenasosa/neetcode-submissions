class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        longest = ""
        
        # even length palidromes would start at the same char consecutively
        for i in range(0, len(s) - 1):
            j = i + 1
            while i >= 0 and j < len(s) and s[i] == s[j]:
                longest = max(longest, s[i:j+1], key=len)
                i -= 1
                j += 1

        # for odd length palindromes, the left and right char are the same
        for i in range(0, len(s) - 1):
            j = i
            while i >= 0 and j < len(s) and s[i] == s[j]:
                longest = max(longest, s[i:j+1], key=len)
                i -= 1
                j += 1

        return longest