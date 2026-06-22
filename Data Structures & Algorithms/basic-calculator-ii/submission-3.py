class Solution:
    def apply_operation(self, operation: str, a: int, b: int) -> int:
        if operation == "+":
            return a + b
        elif operation == "-":
            return a - b
        elif operation == "*":
             return a * b
        elif operation == "/":
            return a // b

    def calculate(self, s: str) -> int:
        operations_1 = set(['*', '/'])
        operations_2 = set(['+', '-'])

        res = 0
        stack = [] # str and int
        # first pass: handle * and / 

        i = 0
        after_first_pass = ''
        while i < len(s):
            if s[i] == ' ':
                i += 1
            elif s[i].isdigit():
                num_str = ''
                while i < len(s) and (s[i].isdigit() or s[i] == ' '): 
                    if s[i].isdigit():
                        num_str += s[i]
                    i += 1
                stack.append(int(num_str))

                if len(stack) == 3:
                    # this guarantees a, operation, b
                    b = stack.pop()
                    operation = stack.pop()
                    a = stack.pop()
                    value = self.apply_operation(operation, a, b)
                    stack.append(value)

            elif s[i] in operations_1:
                stack.append(s[i])
                i += 1
            elif s[i] in operations_2:
                num = stack.pop()
                after_first_pass += str(num)
                after_first_pass += s[i]
                i += 1

        if stack:
            after_first_pass += str(stack.pop())

        # start anew -> second pass handle + and -
        i = 0
        stack = []
        while i < len(after_first_pass):
            if after_first_pass[i] == ' ':
                i += 1
            elif after_first_pass[i].isdigit():
                num_str = ''
                while i < len(after_first_pass) and (after_first_pass[i].isdigit() or after_first_pass[i] == ' '): 
                    if after_first_pass[i].isdigit():
                        num_str += after_first_pass[i]
                    i += 1
                stack.append(int(num_str))

                if len(stack) == 3:
                    # this guarantees a, operation, b
                    b = stack.pop()
                    operation = stack.pop()
                    a = stack.pop()
                    value = self.apply_operation(operation, a, b)
                    stack.append(value)
            elif after_first_pass[i] in operations_2:
                stack.append(after_first_pass[i])
                i += 1


        if stack:
            return stack.pop()

        return 0