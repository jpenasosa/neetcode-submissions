class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        dp = [0]*(amount+1)
        dp[0] = 1

        for i in range(n):
            coin = coins[i]
            for a in range(1, amount+1):
                if a >= coin :
                    dp[a] += dp[a - coin]

        return dp[amount]
