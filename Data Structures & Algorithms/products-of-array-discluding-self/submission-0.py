class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # build prefix array
        prefixes = [1] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                continue
            prefixes[i] = prefixes[i-1] * nums[i-1]

        print(f"{prefixes=}")

        # build suffix array
        suffixes = [1] * len(nums)
        reversed_nums = nums[::-1]
        for j in range(len(reversed_nums)):
            if j == 0:
                continue

            suffixes[j] = suffixes[j-1] * reversed_nums[j-1]

        suffixes = suffixes[::-1]

        print(f"{suffixes=}")

        products = [prefix * suffix for prefix, suffix in zip(prefixes, suffixes)]

        return products