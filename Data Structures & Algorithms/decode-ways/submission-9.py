class Solution:
    # f(n) = f(n+1) + f(n+2)
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0

        n = len(s)
        dp = [0]*(n+1)
        dp[n] = 1

        for i in range(n-1, -1, -1):
            dp[i] = dp[i+1] if s[i] > "0" else 0
            dp[i] += dp[min(i+2, n)] if (10 <= int(s[i:i+2]) <= 26) else 0

        return dp[0]
