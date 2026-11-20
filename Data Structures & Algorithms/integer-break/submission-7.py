class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0]*(n+1)

        for i in range(2, n+1):
            dp[i] = i-1 if i == n else i
            for j in range(1, i):
                dp[i] = max(dp[i], j*dp[i-j])

        return dp[n]
