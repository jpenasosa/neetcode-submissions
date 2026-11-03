import math

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [math.inf]*amount

        a = b = 0
        for i in range(1, amount+1):
            sub = [dp[i - coin] for coin in coins if i - coin >= 0]
            dp[i] = 1 + min(sub, default=math.inf)

        return dp[-1] if math.isfinite(dp[-1]) else -1