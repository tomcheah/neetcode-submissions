class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # monotonically increasing stack (i, height)
        stack.append((-1, 0)) # height of 0 for virtual left boundary
        heights.append(0) # height of 0 for virtual right boundary
        max_area = 0

        for i, height in enumerate(heights):
            while stack and stack[-1][1] > height:
                _, right_height = stack.pop()
                left_i = stack[-1][0]
                width = i - left_i - 1
                area = width * right_height
                max_area = max(max_area, area)

            stack.append((i, height))




        return max_area