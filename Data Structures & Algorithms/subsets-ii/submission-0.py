class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        '''
        Sort first, then do backtracking
        '''
        nums.sort()
        res = []
        subset = []

        def dfs(i: int) -> None:
            res.append(subset.copy())

            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j-1]:
                    continue

                subset.append(nums[j])
                dfs(j+1)
                subset.pop()

        
        dfs(0)
        return res