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

            ways = []
            for coin in coins:
                ways.append(1 + helper(remaining - coin))

            dp[remaining] = min(ways)

            return dp[remaining]
            
        coins = helper(amount)
        if coins == float('inf'):
            return -1
        return coins