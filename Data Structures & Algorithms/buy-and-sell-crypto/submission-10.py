class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mx_profit = 0
        buy = 0
        sell = 0
        while sell < len(prices):
            if prices[sell] <= prices[buy]:
                buy = sell
            else:
                profit = prices[sell] - prices[buy]
                mx_profit = max(profit, mx_profit)
            sell += 1
        return mx_profit
        