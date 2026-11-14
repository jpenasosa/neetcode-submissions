class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = s[0]

        for n in range(len(s)-1):
            # check even length palindromes
            i, j = n, n+1
            while i >= 0 and j < len(s) and s[i] == s[j]:
                ans = max(ans, s[i:j+1], key=len)
                i -= 1
                j += 1

            d = 1
            while n-d >= 0 and n+d < len(s) and s[n-d] == s[n+d]:
                ans = max(ans, s[n-d:n+d+1], key=len)
                d += 1

        return ans
