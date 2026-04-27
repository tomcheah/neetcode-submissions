from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Frequency Array = [min(nums) -> max(nums)]

        Increment each
        """
        num_to_frequency = defaultdict(int)

        for num in nums:
            num_to_frequency[num] += 1

        max_frequency = max(num_to_frequency.values())
        frequency_array = [set() for i in range(max_frequency+1)]
        for num, frequency in num_to_frequency.items():
            frequency_array[frequency].add(num)

        top_k_frequent_values = []
        count = 0

        for num_list in frequency_array[::-1]:
            if not num_list:
                continue 

            if count == k:
                return top_k_frequent_values
            
            top_k_frequent_values.extend(num_list)
            count += len(num_list)

        return top_k_frequent_values
