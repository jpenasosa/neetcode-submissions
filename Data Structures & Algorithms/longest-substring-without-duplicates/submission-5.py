class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        longest = 1
        l, r = 0, 1
        seen = set()
        seen.add(s[l])

        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                r += 1
            else:
                longest = max(longest, len(seen))
                seen.discard(s[l])
                l += 1
                seen.add(s[l])
                r = l + 1 if r <= l else r

        return max(len(seen), longest)
