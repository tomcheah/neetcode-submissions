class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        candidates.sort() 

        def helper(i: int, remaining: int, path: List[int]) -> None:
            if remaining == 0:
                combinations.append(path[:])
                return
            
            if i >= len(candidates):
                return 

            if remaining < 0:
                return

            # take i 
            path.append(candidates[i])
            helper(i+1, remaining - candidates[i], path)
            path.pop()


            # skip i entirely
            next_i = i + 1
            while next_i < len(candidates) and candidates[i] == candidates[next_i]:
                next_i += 1

            helper(next_i, remaining, path)






        helper(0, target, [])
        return combinations