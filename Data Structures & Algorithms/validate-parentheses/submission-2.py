class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        stack = []
        for char in s:
            if char in parentheses:
                if not stack:
                    return False
                item = stack.pop()
                if item != parentheses[char]:
                    return False
                    
            else:
                stack.append(char)



        return len(stack) == 0
