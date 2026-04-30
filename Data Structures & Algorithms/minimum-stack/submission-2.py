class MinStack:
    '''
    Use 2 stacks to maintain pairing between the items in the stack and its associated min
    '''

    def __init__(self):
        self.num_stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        curr_min = val
        if self.min_stack:
            prev_min = self.min_stack[-1]
            curr_min = min(val, prev_min)

        self.num_stack.append(val)
        self.min_stack.append(curr_min)

    def pop(self) -> None:
        self.num_stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.num_stack[-1]
        
    def getMin(self) -> int:
        return self.min_stack[-1]
