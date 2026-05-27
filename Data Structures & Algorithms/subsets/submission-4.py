class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = [] 

        def dfs(i: int) -> None:
            if i == len(nums):
                res.append(subset.copy())
                return

            # take the number
            subset.append(nums[i])
            dfs(i+1)

            # skip the number by undoing the choice
            subset.pop()
            dfs(i+1)

        dfs(0)
        return res