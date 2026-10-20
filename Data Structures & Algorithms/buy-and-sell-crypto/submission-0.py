class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]

        l , r = 0, 1
        while r < len(prices):
            if prices[r] < buy:
                l = r
                r = l + 1
                buy = prices[l]
            else:
                sell = prices[r]
                profit = max(profit, sell - buy)            
                r += 1

        return profit
        