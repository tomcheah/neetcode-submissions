class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combinations = []
        combination = []

        def dfs(i: int, curr_sum: int) -> None:
            if curr_sum > target:
                return

            if curr_sum == target:
                combinations.append(combination.copy())
                return

            if i > len(nums) - 1:
                return

            # take the number and stay at i b/c nums[i] can be reused
            combination.append(nums[i])
            dfs(i, curr_sum + nums[i])

            # skip the number entirely
            combination.pop()
            dfs(i+1, curr_sum)

        dfs(0, 0)
        return combinations