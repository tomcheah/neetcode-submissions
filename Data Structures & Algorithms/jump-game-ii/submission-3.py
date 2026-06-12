class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        l, r = 0, 0 # current layer/ window of reachable elements with {jumps} jumps

        while r < len(nums) - 1:
            farthest = 0

            # given all the values in my window, what is the farthest I can jump to?
            for i in range(l, r+1):
                farthest = max(farthest, i + nums[i])

            # update window
            l = r + 1
            r = farthest
            jumps += 1

        return jumps