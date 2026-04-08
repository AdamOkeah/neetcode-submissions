class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l = 0
        max_profit = 0

        for r in range(1, len(prices)):  # r is sell index
            # if current price is lower than our buy price, move buy pointer
            if prices[r] < prices[l]:
                l = r
            else:
                profit = prices[r] - prices[l]
                if profit > max_profit:
                    max_profit = profit

        return max_profit



      

        