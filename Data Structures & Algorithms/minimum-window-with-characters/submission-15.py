class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans = ""
        target = {}
        captured = {}

        # track needed characters including repeated characters
        for c in t:
            target[c] = 1 + target.get(c, 0)

        # Initialize search
        need = len(target)
        have = 0
        i, j = 0, 0
        for j in range(len(s)):
            c = s[j]
            if c in target:
                captured[c] = 1 + captured.get(c, 0)
                have += (captured[c] == target[c])

            if have == need:
                substr = s[i:j+1]
                ans = min(ans, substr, key=len) if ans else substr

                while i < j and (have == need or s[i] not in target):
                    if s[i] in captured:
                        captured[s[i]] -= 1
                        have -= (captured[s[i]] < target[s[i]])
                    i += 1
                    if have == need:
                        ans = min(ans, s[i:j+1], key=len)

            elif sum(captured.values()) == 0:
                i = j+1

        return ans
