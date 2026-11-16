import math

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}

        def dfs(amount):
            if amount in cache:
                return cache[amount]
            res = math.inf
            if amount < 0:
                return res
            
            if amount == 0:
                return 0

            res = 1 + min(dfs(amount - coin) for coin in coins)
            cache[amount] = res
            return res

        ans = dfs(amount)
        return ans if math.isfinite(ans) else -1