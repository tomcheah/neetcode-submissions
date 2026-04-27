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

        suffix = everything after i multiplied together 
        '''
        prefix_array = [1 for _ in range(len(nums))]
        suffix_array = [1 for _ in range(len(nums))]
        for i in range(len(nums)):
            prefix = 1
            for j in range(i):
                prefix *= nums[j]
            prefix_array[i] = prefix
            suffix = 1
            for k in range(i+1, len(nums)):
                suffix *= nums[k]
            suffix_array[i] = suffix

        output = [prefix_array[i] * suffix_array[i] for i in range(len(nums))]
        return output