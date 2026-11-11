class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [0]*n
        dp[0] = piles[0]
        dp[n-1] = piles[n-1]

        for i in range(1, n//2):
            j = n-1-i
            dp[i] = max(piles[i] + dp[i-1], piles[j] + dp[j+1])

        return dp[n//2-1] > 0
