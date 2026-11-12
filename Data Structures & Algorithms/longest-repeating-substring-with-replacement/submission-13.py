from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 1

        i = 0
        counts = defaultdict(int)
        for j in range(len(s)):
            length = j+1-i
            counts[s[j]] += 1

            if length - max(counts.values()) > k:
                counts[s[i]] -= 1
                i += 1
            else:
                ans = max(ans, length)

        return ans