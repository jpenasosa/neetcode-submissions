from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans = ""
        count_t = defaultdict(int)
        for char in t:
            count_t[char] += 1

        have = 0
        need = len(count_t)
        count = defaultdict(int)
        i = 0
        for j in range(len(s)):
            char = s[j]
            count[char] += 1
            if char in count_t and count[char] == count_t[char]:
                have += 1

            while have == need:
                ans = min(ans, s[i:j+1], key=len) if ans else s[i:j+1]

                count[s[i]] -= 1
                if s[i] in count_t and count[s[i]] < count_t[s[i]]:
                    have -= 1

                i += 1

        return ans
