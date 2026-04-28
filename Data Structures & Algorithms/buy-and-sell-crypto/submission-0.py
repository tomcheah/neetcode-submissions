from math import inf

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        Have to choose one day to buy and one day to sell

        profit = sell - buy

        Let's fix the sell day 

        For each sell day, what is the optimal buy day that will maximize profit? 

        Keep track of cheapest price so far, best profit so far

        new_cheapest = min(old_cheapest, today's price)
        '''

        cheapest_so_far = inf
        best_profit = 0
        for price in prices:
            cheapest_so_far = min(cheapest_so_far, price)
            profit_today = price - cheapest_so_far
            best_profit = max(best_profit, profit_today)

        return best_profit