class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        included_in_path = set()

        def helper(path: List[int]) -> None:
            if len(path) == len(nums):
                permutations.append(path[:])
                return

            for num in nums:
                if num in included_in_path:
                    continue

                included_in_path.add(num)
                path.append(num)
                helper(path)
                path.pop()
                included_in_path.remove(num)
            
        
        helper([])
        return permutations