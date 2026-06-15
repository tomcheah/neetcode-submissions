class Solution:
    def isValid(self, s: str) -> bool:
        parantheses = {
            '(': ')',
            '{': '}', 
            '[': ']'
        }
        opening = set(['(', '{', '['])
        closing = set([')', '}', ']'])

        stack = []
        for char in s:
            if char in opening:
                stack.append(char)

            if char in closing:
                if not stack:
                    return False
                
                top_char = stack.pop()
                if parantheses[top_char] != char:
                    return False

        return len(stack) == 0