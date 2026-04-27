class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        products = [prefix * suffix] at each i

        prefix[i] = nums[i-1] * prefix[i-1]

        suffix[i] = reversed_nums[i-1] * suffix[i-1]
        - Then reverse this
        """
        # build prefix and suffix array
        prefixes = [1] * len(nums)
        suffixes = [1] * len(nums)
        reversed_nums = nums[::-1]
        print(reversed_nums)
        for i in range(len(nums)):
            if i == 0:
                continue
            prefixes[i] = prefixes[i-1] * nums[i-1]
            suffixes[i] = suffixes[i-1] * reversed_nums[i-1]

        suffixes = suffixes[::-1]
        products = [prefix * suffix for prefix, suffix in zip(prefixes, suffixes)]

        return products