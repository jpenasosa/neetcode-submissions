class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l = r = 0
        seen = set()

        while r < len(s):
            while s[r] in seen:
                seen.discard(s[l])
                l += 1

            seen.add(s[r])
            longest = max(longest, r - l + 1)
            r += 1

        return longest
