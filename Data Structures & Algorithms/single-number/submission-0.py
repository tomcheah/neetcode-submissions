class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        val = nums[0]
        for i in range(1, len(nums)):
            val = val ^ nums[i]

        return val