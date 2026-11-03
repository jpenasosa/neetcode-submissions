import math

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}

        def make_change(i, amount):
            args = (i, amount)
            if args in cache:
                return cache[args]

            if amount == 0: return 0
            if amount < 0 or i >= len(coins): return math.inf

            ans = min(1 + make_change(i, amount - coins[i]), make_change(i+1, amount))
            cache[args] = ans
            return ans

        count = make_change(0, amount)
        return -1 if math.isinf(count) else count
