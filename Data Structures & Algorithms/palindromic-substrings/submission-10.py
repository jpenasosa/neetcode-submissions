class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = len(s)
        for n in range(len(s)-1):
            # even length palindromes
            i, j = n, n+1
            while i >= 0 and j < len(s) and s[i] == s[j]:
                ans += 1
                i -= 1
                j += 1

            # odd length palindromes
            i, j = n-1, n+1
            while i >= 0 and j < len(s) and s[i] == s[j]:
                ans += 1
                i -= 1
                j += 1

        return ans