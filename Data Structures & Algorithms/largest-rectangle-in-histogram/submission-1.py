class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i, height in enumerate(heights):
            # process items if curr bar is smaller than top of stack
            while stack and height < stack[-1][1]:
                popped_index, popped_height = stack.pop()

                # we cannot include the right bar itself
                right_bound = i - 1

                left_bound = 0
                if stack:
                    # we cannot include the left bar itself
                    left_bound = stack[-1][0] + 1

                # we add one to account for the bar itself
                width = right_bound - left_bound + 1
                area = popped_height * width
                max_area = max(area, max_area)

            stack.append((i, height))

        # process bars that never found a smaller bar on the right
        while stack:
            popped_index, popped_height = stack.pop()

            right_bound = len(heights) - 1

            left_bound = 0
            if stack:
                left_bound = stack[-1][0] + 1 

            width = right_bound - left_bound + 1
            area = popped_height * width
            max_area = max(area, max_area)

        return max_area