from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = defaultdict() # value: index
        for i, num in enumerate(nums):
            value = target - num
            if value in seen:
                first_index = seen[value]
                return [first_index, i]
            seen[num] = i
            


