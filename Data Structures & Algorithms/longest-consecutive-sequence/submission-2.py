class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        starting num = one where {num - 1} does not exist in the sequence
        - only need to check starting nums
        '''
        nums_set = set(nums)
        longest_count = 0
        # iterate through each num only once
        for num in nums_set: 
            previous_num = num - 1
            # found a starting num
            if previous_num not in nums_set:
                subsequence_length = 1
                next_num = num + 1
                while next_num in nums_set:
                    subsequence_length += 1
                    next_num += 1
                longest_count = max(longest_count, subsequence_length)

        return longest_count