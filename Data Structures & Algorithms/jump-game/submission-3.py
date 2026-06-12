class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
        Among all places I can currently reach, how far can my reachable zone expand?

        At each step, we greedily keep the best possible reach

        At each reachable index, the only useful information is how far it can extend our reach.
        '''
        farthest = 0

        for i in range(len(nums)):
            if i > farthest:
                return False

            farthest = max(farthest, i + nums[i])
            if farthest >= len(nums) - 1:
                return True

        
        return True

        