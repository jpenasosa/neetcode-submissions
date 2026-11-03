class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        
        def countPalindromes(i, j):
            count = 0
            while i >= 0 and j < len(s) and s[i] == s[j]:
                count += 1
                i -= 1
                j += 1
            
            return count

        for i in range(len(s)):
            # even length palindromes
            ans += countPalindromes(i, i + 1)

            # odd length palindromes
            ans += countPalindromes(i, i)

        return ans
