class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def helper(i: int, curr_sum: int) -> int:
            if i == len(nums):
                if curr_sum == target:
                    return 1
                else:
                    return 0

            take_add = helper(i+1, curr_sum + nums[i])
            take_subtract = helper(i+1, curr_sum - nums[i])

            return take_add + take_subtract

        return helper(0, 0)
