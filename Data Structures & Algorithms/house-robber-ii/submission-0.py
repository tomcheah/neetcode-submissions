class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_linear(arr: List[int]) -> int:
            cache = {}
            def helper(i: int) -> int:
                '''
                Returns the maximum amount made from position i to the end

                Recurrence relation: 
                helper(i) = max(
                    nums[i] + helper(i+2), # take
                    helper(i+1), skip
                )
                '''
                if i >= len(arr):
                    return 0

                if i in cache:
                    return cache[i]

                # take house i 
                take = arr[i] + helper(i+2)

                # skip house i
                skip = helper(i+1)

                cache[i] = max(take, skip)
                return cache[i]

            return helper(0)

        if len(nums) == 1:
            return nums[0]
            
        # we either exclude the first or the last house
        exclude_last = rob_linear(nums[0:len(nums)-1])
        exclude_first = rob_linear(nums[1:])

        return max(exclude_last, exclude_first)