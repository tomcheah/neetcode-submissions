class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        buying == True  -> allowed to buy / currently not holding
        buying == False -> must sell before buying again / currently holding

        At each day, we are either holding stock or not holding stock

        Not holding stock:
        - buy
        - skip

        Holding stock:
        - sell
        - skip
        '''

        dp = {} # (i, buying) -> max profit

        def helper(i: int, buying: bool) -> int:
            if i >= len(prices):
                return 0

            if (i, buying) in dp:
                return dp[(i, buying)]

            # doing nothing on day i 
            skip = helper(i+1, buying)
            if buying:
                buy = helper(i+1, not buying) - prices[i]
                dp[(i, buying)] = max(buy, skip)
            else:
                sell = helper(i+2, not buying) + prices[i]
                dp[(i, buying)] = max(sell, skip)

            return dp[(i, buying)]
        
        return helper(0, True)