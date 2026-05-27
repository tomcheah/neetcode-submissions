class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(i: int, path: List[int]) -> None:
            if i == len(nums):
                res.append(path)
                return

            # skip item
            helper(i+1, path)

            # take item
            helper(i+1, path + [nums[i]])

        helper(0, [])

        return res