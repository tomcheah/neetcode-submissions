class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
        Start at the end and see if we can work our way to the beginning

        From this index, I can eventually reach the last index.

        Can index i reach the nearest known-good position?

        If the current index can reach the current goal, immediately make the current index the new goal.
        '''
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1 ,-1):
            # can I reach my goal from i?
            if goal <= i + nums[i]:
                goal = i

        return goal == 0

        