class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        def helper(remaining: int) -> int:
            if remaining in dp:
                return dp[remaining]
            
            if remaining == 0:
                return 0
            
            if remaining < 0:
                return float('inf')

            best = float('inf')
            for coin in coins:
                best = min(best, 1 + helper(remaining - coin))

            dp[remaining] = best
            return best
            
        res = helper(amount)
        return -1 if res == float('inf') else res