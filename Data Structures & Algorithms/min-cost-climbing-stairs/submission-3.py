class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)

        def climb(cost):
            n = len(cost)
            dp = [0]*n
            dp[0] = cost[0]
            dp[1] = cost[1] + cost[0]

            for i in range(2, n):
                dp[i] = cost[i] + min(dp[i-1], dp[i-2])

            return dp[n-1]
        
        return min(climb(cost), climb(cost[1:]))

