from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans = ""
        target = defaultdict(int)
        captured = defaultdict(int)

        # track needed characters including repeated characters
        for c in t:
            target[c] += 1

        # Initialize search
        need = len(target)
        have = 0
        i = 0
        for j in range(len(s)):
            c = s[j]
            captured[c] += 1
            if c in target and captured[c] == target[c]:
                have += 1

            while have == need:
                substr = s[i:j+1]
                ans = min(ans, substr, key=len) if ans else substr

                captured[s[i]] -= 1
                if s[i] in captured and captured[s[i]] < target[s[i]]:
                    have -= 1

                i += 1

        return ans
