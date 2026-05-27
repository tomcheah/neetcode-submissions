class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        permutation = []

        def dfs() -> None:
            if len(permutation) == len(nums):
                res.append(permutation.copy())
                return

            for i in range(len(nums)):
                if nums[i] in permutation:
                    continue
                
                permutation.append(nums[i])
                dfs()
                permutation.pop()

        dfs()
        return res