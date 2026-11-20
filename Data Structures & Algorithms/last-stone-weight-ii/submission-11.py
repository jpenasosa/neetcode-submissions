class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)
        total = sum(stones)
        target = total // 2

        dp = [[0]*(target+1) for _ in range(n)]

        for t in range(target+1):
            if t < stones[0]:
                continue
            dp[0][t] = stones[0]

        for i in range(1, n):
            for t in range(target+1):
                dp[i][t] = dp[i-1][t] # Skip current stone
                if t >= stones[i]:  # Include current stone
                    dp[i][t] = max(dp[i][t], stones[i] + dp[i-1][t - stones[i]])

        res = dp[-1][target]
        return total - 2*res
