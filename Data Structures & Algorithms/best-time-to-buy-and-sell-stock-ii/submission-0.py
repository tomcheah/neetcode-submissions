class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cash = [0] * len(prices)
        hold = [0] * len(prices)

        cash[0] = 0
        hold[0] = -prices[0]

        for i in range(1, len(prices)):
            cash[i] = max(cash[i-1], hold[i-1] + prices[i])
            hold[i] = max(hold[i-1], cash[i-1] - prices[i])

        return cash[-1]