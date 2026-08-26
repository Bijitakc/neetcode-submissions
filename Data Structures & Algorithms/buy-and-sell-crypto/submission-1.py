class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = None
        cheapest = prices[0]
        for i in range(len(prices)):
            curr_profit = prices[i] - cheapest
            if not prof or curr_profit > prof:
                prof = curr_profit
            if prices[i] < cheapest:
                cheapest = prices[i]
        return prof if prof > 0 else 0
