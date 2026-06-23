class Solution:
    def decodeString(self, s: str) -> str:
        string_stack = []
        count_stack = []
        res = ''

        multiplier = 0

        for char in s:
            if char.isdigit():
                multiplier = multiplier * 10 + int(char)

            elif char == '[':
                string_stack.append(res)
                count_stack.append(multiplier)
                multiplier = 0
                res = ''
            elif char == ']':
                prev_string = string_stack.pop()
                repeat_count = count_stack.pop()
                res = f'{prev_string}{repeat_count * res}'
            else:
                res += char


        return res
    
            


        