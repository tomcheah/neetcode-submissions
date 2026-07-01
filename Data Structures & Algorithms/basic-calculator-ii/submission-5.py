class Solution:
    def calculate(self, s: str) -> int:
        operations = set(['+', '-', '*', '/'])
        # remove whitespaces 
        s = s.replace(' ', '')

        stack = [] 
        i = 0
        num = 0
        previous_operation = '+'

        for i, char in enumerate(s):
            if char.isdigit():
                num = num * 10 + int(char)

            if char in operations or i == len(s) - 1:
                if previous_operation == '+':
                    stack.append(num)
                elif previous_operation == '-':
                    stack.append(-num)
                elif previous_operation == '*':
                    prev_val = stack.pop()
                    stack.append(prev_val * num)
                else:
                    prev_val = stack.pop()
                    stack.append(int(prev_val / num))
                
                previous_operation = char
                num = 0

        return sum(stack)
