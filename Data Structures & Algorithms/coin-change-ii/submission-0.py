class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        '''
        (i, remaining)
        - i = the current coin we are allowed to consider
        - remaining = the amount left to build
        '''
        dp = {}

        def helper(i: int, remaining: int) -> int:
            if remaining == 0:
                return 1

            if remaining < 0:
                return 0

            if i >= len(coins):
                return 0

            if (i, remaining) in dp:
                return dp[(i, remaining)]

            # use this coin again
            take = helper(i, remaining - coins[i])

            # move onto the next coin
            skip = helper(i+1, remaining)

            dp[(i, remaining)] = take + skip
            return dp[(i, remaining)]


        return helper(0, amount)