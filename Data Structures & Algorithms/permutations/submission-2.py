class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums_set = set(nums)

        def helper(remaining: set[int], path: List[int]) -> None:
            if len(remaining) == 0:
                res.append(path[:])
                return

            remaining = remaining.copy()

            for num in remaining: 
                path.append(num)
                remaining.discard(num)
                helper(remaining, path) 
                remaining.add(num)
                path.pop()
                

        helper(nums_set, [])
        return res