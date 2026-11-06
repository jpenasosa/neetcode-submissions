class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        low = prices[0]

        for i in range(1, len(prices)):
            cur, prev = prices[i], prices[i-1]
            if cur < prev:
                profit += prev - low
                low = cur
            else:
                low = min(low, cur)

        # Sell last position
        return profit + (prices[-1] - low)
