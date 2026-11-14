class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = s[0]
        max_length = 1

        for n in range(len(s)-1):
            # check even length palindromes
            i, j = n, n+1
            while i >= 0 and j < len(s) and s[i] == s[j]:
                length = j+1-i
                if length > max_length:
                    ans = s[i:j+1]
                    max_length = length

                i -= 1
                j += 1

            i, j = n-1, n+1
            while i >= 0 and j < len(s) and s[i] == s[j]:
                length = j+1-i
                if length > max_length:
                    ans = s[i:j+1]
                    max_length = length

                i -= 1
                j += 1

        return ans
