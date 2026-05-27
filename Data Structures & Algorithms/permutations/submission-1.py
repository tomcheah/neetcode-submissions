class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        permutation = []

        def dfs() -> None:
            if len(permutation) == len(nums):
                res.append(permutation.copy())
                return

            for num in nums:
                if num in permutation:
                    continue
                
                permutation.append(num)
                dfs()
                permutation.pop()

        dfs()
        return res