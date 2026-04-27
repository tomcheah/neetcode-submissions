class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Store map num -> index

        You have current index 

        You want previous index 

        At the current iteration, you have target - num = item_you_want 

        """

        num_to_index = {}

        for i, num in enumerate(nums):
            curr_diff = target - num
            if curr_diff in num_to_index:
                return [num_to_index[curr_diff], i]
            else:
                num_to_index[num] = i

