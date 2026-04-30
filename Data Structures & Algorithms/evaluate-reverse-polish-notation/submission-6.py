import operator


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": lambda a, b: int(a/b)
        }

        num_stack = []
        operand_stack = []

        for token in tokens:
            print(f'{token=}')
            if token in ops:
                second_val = num_stack.pop()
                first_val = num_stack.pop()
                result = ops[token](first_val, second_val)
                num_stack.append(result)
            else:
                num = int(token)
                num_stack.append(num)

        print(num_stack)
        return num_stack.pop()
