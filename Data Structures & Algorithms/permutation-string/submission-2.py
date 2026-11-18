from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        n = len(s2)
        size = len(s1)

        target = defaultdict(int)
        for c in s1:
            target[c] += 1

        need = len(target)
        have = 0

        cur = defaultdict(int)
        for c in s2[:size]:
            cur[c] += 1
            if c in target and cur[c] == target[c]:
                have += 1

        if have == need:
            return True

        i = 0
        for c in s2[size:]:
            prev = s2[i]
            if prev in target and cur[prev] == target[prev]:
                have -= 1

            cur[prev] -= 1
            cur[c] += 1
            if c in target and cur[c] == target[c]:
                have += 1

            if have == need:
                return True
            
            i += 1

        return False
