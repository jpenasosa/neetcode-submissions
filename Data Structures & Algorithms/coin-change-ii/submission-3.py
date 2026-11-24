class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        # dp = [[0]*(amount+1) for _ in range(n+1)]
        # for i in range(1, n+1):        
        # return dp[n][amount]

        cache = {}
        def dfs(i, amount):
            if (i, amount) in cache:
                return cache[(i, amount)]

            if i == n or amount < 0:
                return 0

            if amount == 0:
                return 1

            res = dfs(i, amount-coins[i]) + dfs(i+1, amount)
            cache[(i, amount)] = res
            return res
        
        return dfs(0, amount)
