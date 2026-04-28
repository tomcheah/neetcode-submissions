class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        heights = [1,7,2,5,4,7,3,6]

        How can I make use of 2 pointers?

        area = min(height_1, height_2) * width
        
        maximize the width by instantiating l and r to ends of the arrays

        then decrement and see if there's anything better

        Because we maximized width, the only thing to optimize left is height
        '''
        l, r = 0, len(heights) - 1
        max_water = 0
        while l < r:
            container_height = min(heights[l], heights[r])
            container_width = r - l
            curr_water = container_height * container_width
            if heights[l] > heights[r]:
                r -= 1
            else: 
                l += 1
            max_water = max(curr_water, max_water)

        return max_water