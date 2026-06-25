class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        used = set()
        def helper(path: List[int]) -> None:
            if len(path) == len(nums):
                permutations.append(path[:])
                return

            for num in nums:
                if num in used:
                    continue 

                used.add(num)
                path.append(num)
                helper(path)
                path.pop()
                used.remove(num)

        helper([])
        return permutations