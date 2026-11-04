class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = {}

        def word_break(i):
            if i in cache:
                return cache[i]

            if i  >= len(s):
                return True

            res = False
            for word in wordDict:
                if not s[i:].startswith(word):
                    continue

                if word_break(i+len(word)):
                    res = True
                    break

            cache[i] = res
            return res

        return word_break(0)
