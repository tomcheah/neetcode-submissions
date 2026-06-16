class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        def helper(i: int) -> int:
            if i in dp:
                return dp[i]

            if i >= len(nums):
                return 0

            # take 
            take = nums[i] + helper(i+2)

            # skip 
            skip = helper(i+1)

            dp[i] = max(take, skip)

            return dp[i]

        return helper(0)