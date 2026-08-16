class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        cheapest_day_price = prices[0]
        max_profit = 0 
        for i in range(0, n):
            cheapest_day_price = min(prices[i], cheapest_day_price)
            today_profit = prices[i] - cheapest_day_price
            max_profit = max(max_profit, today_profit)
        return max_profit