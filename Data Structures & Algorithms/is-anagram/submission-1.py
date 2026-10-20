from collections import defaultdict

class Solution:
    def getCounts(self, string: str) -> Dict[str, int]:
        counts = defaultdict(int)
        for n in string:
            counts[n] += 1
        
        return counts

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_s = self.getCounts(s)
        count_t = self.getCounts(t)

        if len(count_s) != len(count_t):
            return False

        for char in count_s:
            if count_s[char] != count_t[char]:
                return False
        
        return True