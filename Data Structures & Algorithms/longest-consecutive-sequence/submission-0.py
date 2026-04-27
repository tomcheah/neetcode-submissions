class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)

        longest_sequence_length = 0
        sequence_start_num = 0
        for num in nums:
            if num - 1 not in num_set:
                # we found the start of a sequence
                sequence_start_num = num
                consecutive_sequence = [sequence_start_num]
                while True: 
                    if sequence_start_num + 1 in num_set:
                        consecutive_sequence.append(sequence_start_num)
                        sequence_start_num += 1
                    else:
                        break

                longest_sequence_length = max(longest_sequence_length, len(consecutive_sequence))
                    

        return longest_sequence_length