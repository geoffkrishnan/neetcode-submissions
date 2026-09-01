class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        curr_stock = prices[0]
        for i in range(1, len(prices)):
            if prices[i] > curr_stock:
                max_profit += prices[i] - curr_stock
            curr_stock = prices[i]


        return max_profit 