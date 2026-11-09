class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0]*(n+1)

        for i in range(1, n+1):
            dp[i] = i if i < n else 0
            for j in range(1, n//2 + 1):
                dp[i] = max(dp[i], dp[j] * dp[i-j])

        return dp[n]
