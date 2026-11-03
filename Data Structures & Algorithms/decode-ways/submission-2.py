class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0

        cache = {}

        def decodings(s):
            if not s:
                return 1

            if s in cache:
                return cache[s]

            if len(s) == 1:
                return 1 if s != "0" else 0

            count = 0 if s[0] == "0" else decodings(s[1:])
            count += 0 if int(s[:2]) < 10 or int(s[:2]) > 26 else decodings(s[2:])

            cache[s] = count
            return count
        
        return decodings(s)
