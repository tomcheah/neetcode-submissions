class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        max_volume = 0
        while l < r:
            curr_volume = min(heights[l], heights[r]) * (r-l)
            max_volume = max(max_volume, curr_volume)
            # Update rule
            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                # arbitrary
                l += 1

        return max_volume
