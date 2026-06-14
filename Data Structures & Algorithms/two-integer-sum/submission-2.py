class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_to_index = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in value_to_index:
                return [value_to_index[complement], i]
            else:
                value_to_index[num] = i

