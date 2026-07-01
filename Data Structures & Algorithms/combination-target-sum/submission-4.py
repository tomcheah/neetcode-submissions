class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combinations = []

        def helper(i: int, remaining: int, path: List[int]) -> None:
            if remaining < 0:
                return 

            if remaining == 0:
                combinations.append(path[:])
                return

            if i >= len(nums):
                return

            # take i 
            path.append(nums[i])
            helper(i, remaining - nums[i], path)
            path.pop()

            # skip i
            helper(i+1, remaining, path)

        helper(0, target, [])
        return combinations