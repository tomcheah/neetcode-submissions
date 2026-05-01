class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                stack_i, stack_temp = stack.pop()
                distance = i - stack_i
                result[stack_i] = distance

            stack.append((i, temp))

        return result