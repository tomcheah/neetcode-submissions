class Solution:
    def trap(self, height: List[int]) -> int:
        # bottleneck is min(height[l], height[r])
        if not height:
            return 0

        l, r = 0, len(height) - 1
        left_max, right_max = height[l], height[r]
        total_water = 0
        while l < r:
            water_at_curr_position = 0
            if left_max < right_max:
                l += 1
                left_max = max(left_max, height[l])
                # this will never be negative because left_max >= height[l] due to update above
                water_at_curr_position = left_max - height[l]
            else:
                r -= 1
                right_max = max(right_max, height[r])
                # this will never be negative because right_max >= height[r] due to update above
                water_at_curr_position = right_max - height[r]
            
            total_water += water_at_curr_position



        return total_water