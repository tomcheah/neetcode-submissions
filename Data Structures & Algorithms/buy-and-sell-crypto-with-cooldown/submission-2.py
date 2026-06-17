class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        can_buy == True  -> allowed to buy / currently not holding
        can_buy == False -> must sell before buying again / currently holding

        At each day, we are either holding stock or not holding stock

        Not holding stock:
        - buy
        - skip

        Holding stock:
        - sell
        - skip
        '''

        dp = {} # (i, can_buy) -> max profit

        def helper(i: int, can_buy: bool) -> int:
            if i >= len(prices):
                return 0

            if (i, can_buy) in dp:
                return dp[(i, can_buy)]

            # doing nothing on day i 
            skip = helper(i+1, can_buy)
            if can_buy:
                buy = helper(i+1, not can_buy) - prices[i]
                dp[(i, can_buy)] = max(buy, skip)
            else:
                sell = helper(i+2, not can_buy) + prices[i]
                dp[(i, can_buy)] = max(sell, skip)

            return dp[(i, can_buy)]
        
        return helper(0, True)