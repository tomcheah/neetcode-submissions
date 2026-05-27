class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        combination = []

        candidates.sort()

        def dfs(i: int, curr_sum: int) -> None:
            if curr_sum > target:
                return

            if curr_sum == target:
                res.append(combination.copy())
                return

            for j in range(i, len(candidates)):
                # skip dupliate choices at the same recursion level
                if j > i and candidates[j] == candidates[j-1]:
                    continue

                # choose item 
                combination.append(candidates[j])
                # explore
                dfs(j+1, curr_sum+candidates[j])
                # undo choice
                combination.pop()


        dfs(0, 0)
        return res