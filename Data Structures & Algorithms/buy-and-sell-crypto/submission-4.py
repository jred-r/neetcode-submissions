class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        
        profit = 0
        buy = 0
        sell = 1
        while sell < len(prices):
            if prices[sell] < prices[buy]:
                buy = sell
            else:
                profit = max(profit, prices[sell] - prices[buy])

            sell += 1
        return profit

        