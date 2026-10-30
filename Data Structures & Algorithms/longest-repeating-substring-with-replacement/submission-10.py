from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 1
        i, j = 0, 0
        counts = defaultdict(int)

        while j < len(s):
            counts[s[j]] += 1
            while i < j and j+1-i - max(counts.values()) > k:
                counts[s[i]] -= 1
                i += 1

            longest = max(longest, j+1-i)
            j += 1

        return longest
