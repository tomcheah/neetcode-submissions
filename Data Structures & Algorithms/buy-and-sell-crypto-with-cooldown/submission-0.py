class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {} # (i, buying) -> max profit

        def helper(i: int, buying: bool) -> int:
            if i >= len(prices):
                return 0

            if (i, buying) in dp:
                return dp[(i, buying)]

            # doing nothing on day i 
            cooldown = helper(i+1, buying)
            if buying:
                buy = helper(i+1, not buying) - prices[i]
                dp[(i, buying)] = max(buy, cooldown)
            else:
                sell = helper(i+2, not buying) + prices[i]
                dp[(i, buying)] = max(sell, cooldown)

            return dp[(i, buying)]
        
        return helper(0, True)