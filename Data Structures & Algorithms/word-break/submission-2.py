class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [True] + [False]*len(s)

        for i in range(len(s)+1):
            if dp[i] == False:
                continue

            for word in wordDict:
                if s[i:].startswith(word) and dp[i]:
                    dp[i+len(word)] = True

        return dp[-1]
