class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = s[0]
        
        for n in range(0, len(s) - 1):
            # even length palidromes would start at the same char consecutively
            i = n
            j = i + 1
            while i >= 0 and j < len(s) and s[i] == s[j]:
                longest = max(longest, s[i:j+1], key=len)
                i -= 1
                j += 1

            # for odd length palindromes, the left and right char are the same
            i = n
            j = i + 2
            while i >= 0 and j < len(s) and s[i] == s[j]:
                longest = max(longest, s[i:j+1], key=len)
                i -= 1
                j += 1

        return longest