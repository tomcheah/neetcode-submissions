class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = [] # monotonically increasing stack
        heights += [0] # add a boundary to the end
        (1, 0)

        [(0, 1), (1, 0)]

        for i, height in enumerate(heights): 
            if not stack:
                stack.append((i, height))
                continue

            # we encounter a smaller bar
            while stack and stack[-1][1] > height:
                _, prev_height = stack.pop()
                
                # find the left boundary
                left_bar_i = -1
                if stack:
                    left_bar_i = stack[-1][0]

                # not inclusive of left and right bounds
                right_bar_i = i
                length = right_bar_i - left_bar_i - 1

                area = prev_height * length
                res = max(area, res)

            stack.append((i, height))

        return res
        