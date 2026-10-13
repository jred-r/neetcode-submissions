class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #base case
        if len(prices) == 1:
            return 0

        profit = 0
        buy = 0
        sell = 1
        #buy and sell 
        while sell < len(prices):
            if prices[buy] < prices[sell]:
                profit = max(profit, prices[sell] - prices[buy])
            else:
                buy = sell
            sell += 1
        
        return profit

        