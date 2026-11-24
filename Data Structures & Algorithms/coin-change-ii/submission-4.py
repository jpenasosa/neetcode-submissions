class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        dp = [[0]*(amount+1) for _ in range(n)]

        for i in range(n):
            dp[i][0] = 1

        for i in range(n):
            coin = coins[i]
            for a in range(1, amount+1):
                res = dp[i-1][a]
                if a >= coin :
                    res += dp[i][a - coin]
                dp[i][a] = res

        return dp[-1][amount]
