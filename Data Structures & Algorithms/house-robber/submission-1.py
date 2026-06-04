class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        def helper(i: int) -> int:
            '''
            Returns maximum amount of money from position i to the end

            Recurrence relation:
            helper(i) = max(
                nums[i] + helper(i+2), # take i
                helper(i+1) # skip i
            )
            '''
            if i >= len(nums):
                return 0

            if i in cache:
                return cache[i]

            # take house i 
            take = nums[i] + helper(i+2)

            # skip house i 
            skip = helper(i+1)

            cache[i] = max(skip, take)

            return cache[i]

        return helper(0)
            
            