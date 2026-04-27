class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        Build a prefix array

        Build a suffix array

        Multiply them together or something? 

        [prefix, i, suffix]

        output[i] = prefix * suffix

        How can we calculate this prefix and suffix? 

        prefix = everything before i multipled together
        - Build this iteratively

        suffix = everything after i multiplied together 
        '''
        n = len(nums)
        prefix_array = [1 for _ in range(len(nums))]
        suffix_array = [1 for _ in range(len(nums))]
        for i in range(1, n):
            # the current prefix = new number * cumulative prefix so far
            prefix_array[i] = nums[i - 1] * prefix_array[i-1]
        for i in range(n-2, -1, -1):
            # the current suffix = new number * cumulative suffix so far
            suffix_array[i] = nums[i+1] * suffix_array[i+1]

        output = [prefix_array[i] * suffix_array[i] for i in range(len(nums))]
        return output