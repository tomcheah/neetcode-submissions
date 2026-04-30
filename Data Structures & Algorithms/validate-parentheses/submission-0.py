class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        brackets = {
            ')': '(',
            '}': '{',
            ']': '[',
        }

        closing_brackets = set([')', '}', ']'])
        for char in s:
            if char in closing_brackets:
                if not stack:
                    return False

                bracket = stack.pop()
                matching_bracket = brackets[char]

                if bracket != matching_bracket:
                    return False
            else:
                stack.append(char)

        return len(stack) == 0