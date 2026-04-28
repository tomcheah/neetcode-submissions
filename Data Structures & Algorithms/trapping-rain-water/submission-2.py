class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        water[i] = min(height[l], height[r]) - height[i]
        '''
        l, r = 0, len(height)-1

        # build best heights for each position scanning from left side
        left_max = 0
        left_heights = [0] * len(height)
        for i, curr_height in enumerate(height):
            left_max = max(curr_height, left_max)
            left_heights[i] = left_max

        # build best heights for each position scanning from right side
        right_max = 0
        right_heights = [0] * len(height)
        for i in range(len(height)-1, -1, -1):
            curr_height = height[i]
            right_max = max(curr_height, right_max)
            right_heights[i] = right_max

        trapped_water = [0] * len(height)
        for i in range(len(height)):
            left_max = left_heights[i]
            right_max = right_heights[i]
            trapped_water[i] = min(left_max, right_max) - height[i]

        return sum(trapped_water)