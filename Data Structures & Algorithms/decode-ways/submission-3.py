class Solution:
    def numDecodings(self, s: str) -> int:
        cache = {len(s): 1}

        def decodings(i):
            if i in cache:
                return cache[i]

            if s[i] == "0":
                return 0

            count = decodings(i+1)
            if i+2 <= len(s) and 10 <= int(s[i:i+2]) <= 26:
                count += decodings(i+2)

            cache[i] = count
            return count
        
        return decodings(0)
