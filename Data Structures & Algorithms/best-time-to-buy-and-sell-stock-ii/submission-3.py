class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [0]*(n+1)
        profit = 0
        lo = 0

        for i in range(1, n):
            cur = prices[i]
            dp[i] = max([cur-prices[j] for j in range(lo, i)], default=0)
            if dp[i] < dp[i-1]:
                dp[i] = 0
                profit += max(0, dp[i-1])
                lo = i

        return profit + max(dp[lo+1:])