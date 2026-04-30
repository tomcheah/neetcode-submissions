class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_stack = []
        for token in tokens:
            if token == '+':
                second_val = num_stack.pop()
                first_val = num_stack.pop()
                num_stack.append(first_val + second_val)
            elif token == '-':
                second_val = num_stack.pop()
                first_val = num_stack.pop()
                num_stack.append(first_val - second_val)
            elif token == '*':
                second_val = num_stack.pop()
                first_val = num_stack.pop()
                num_stack.append(first_val * second_val)
            elif token == '/':
                second_val = num_stack.pop()
                first_val = num_stack.pop()
                num_stack.append(int(first_val / second_val))
            else: 
                num_stack.append(int(token))

        return num_stack.pop()