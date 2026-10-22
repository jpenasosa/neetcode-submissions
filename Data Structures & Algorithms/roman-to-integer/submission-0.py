class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        romans = {"I": 1, "V": 5, "X": 10, "L":50, "C": 100, "D": 500, "M": 1000}

        prev = None
        for i in range(len(s)):
            cur = romans[s[i]]
            if prev and prev < cur:
                ans += cur - prev*2
            else:
                ans += cur
            
            prev = cur
        
        return ans