class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combinations = []
        def helper(i: int, remaining: int, path: int) -> None:
            if remaining == 0:
                combinations.append(path[:])
                return
            
            if remaining < 0:
                return

            for j in range(i, len(nums)):
                path.append(nums[j])
                helper(j, remaining - nums[j], path)
                path.pop()

        helper(0, target, [])
        return combinations