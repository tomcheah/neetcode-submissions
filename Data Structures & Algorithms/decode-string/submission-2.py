class Solution:
    def decodeString(self, s: str) -> str:
        string_stack = []
        count_stack = []
        curr_string = ''

        multiplier = 0

        for char in s:
            if char.isdigit():
                multiplier = multiplier * 10 + int(char)

            elif char == '[':
                string_stack.append(curr_string)
                count_stack.append(multiplier)
                multiplier = 0
                curr_string = ''
            elif char == ']':
                prev_string = string_stack.pop()
                repeat_count = count_stack.pop()
                curr_string = f'{prev_string}{repeat_count * curr_string}'
            else:
                curr_string += char


        return curr_string
    
            


        