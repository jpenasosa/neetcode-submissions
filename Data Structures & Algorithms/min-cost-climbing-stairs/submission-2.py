class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # f(0) = cost[0]
        # f(1) = cost[1]
        # f(2) = cost[2] + min(f(0), f(1))

        cost.append(0)

        a, b = cost[0], cost[1]
        for n in range(2, len(cost)):
            a, b = b, cost[n] + min(a, b)

        return b
