class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        candidates.sort() # sort in ascending order to handle duplicates

        def helper(i: int, remaining: int, path: List[int]) -> None:
            if remaining == 0:
                combinations.append(path[:])
                return

            if remaining < 0:
                return 
            
            if i >= len(candidates):
                return

            # take candidates[i]
            path.append(candidates[i])
            helper(i+1, remaining - candidates[i], path)
            path.pop()

            # skip candidates[i] and all duplicates -> find the next index and recurse
            next_i = i + 1
            while next_i < len(candidates) and candidates[next_i] == candidates[i]:
                next_i += 1

            helper(next_i, remaining, path)
            
        helper(0, target, [])
        return combinations