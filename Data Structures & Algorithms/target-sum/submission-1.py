class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def helper(i: int, running_sum: int) -> int:
            if i == len(nums):
                if running_sum == target:
                    return 1
                
                return 0

            add = helper(i+1, running_sum + nums[i])
            subtract = helper(i+1, running_sum - nums[i])

            dp[(i, running_sum)] = add + subtract
            return dp[(i, running_sum)]

        return helper(0, 0)