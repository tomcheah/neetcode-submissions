class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        for i in range(length):
            length ^= i ^ nums[i]

        return length