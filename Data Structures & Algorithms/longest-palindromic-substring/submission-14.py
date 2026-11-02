class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = s[0]
        longest = 1
        
        # even length palidromes would start at the same char consecutively
        for n in range(len(s)):
            i, j = n, n + 1
            while i >= 0 and j < len(s) and s[i] == s[j]:
                if j + 1 - i > longest:
                    res = s[i:j+1]
                    longest = j+1-i

                i -= 1
                j += 1

            # for odd length palindromes, the left and right char are the same
            i, j = n, n + 2
            while i >= 0 and j < len(s) and s[i] == s[j]:
                if j + 1 - i > longest:
                    res = s[i:j+1]
                    longest = j+1-i

                i -= 1
                j += 1

        return res