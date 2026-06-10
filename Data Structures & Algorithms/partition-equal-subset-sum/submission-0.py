class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 == 1:
            return False

        target = total // 2
        dp = {} # (index, remaining)
        
        def helper(i: int, remaining: int) -> bool:
            '''
            Starting at index i, can I form the sum remaining?
            '''
            if i == len(nums):
                return False

            if remaining == 0:
                return True

            if remaining < 0:
                return False

            if (i, remaining) in dp:
                return dp[(i, remaining)]

            take_i = helper(i+1, remaining - nums[i])
            skip_i = helper(i+1, remaining)
            dp[(i, remaining)] = take_i or skip_i

            return dp[(i, remaining)]

        return helper(0, target)