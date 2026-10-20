class MinStack:
    def __init__(self):
        self.min_stack = []
        self.stack = []
        self.size = 0

    def push(self, val: int) -> None:
        if val <= (self.min_stack[-1] if self.min_stack else val):
            self.min_stack.append(val)
        self.stack.append(val)
        self.size += 1

    def pop(self) -> None:
        num = self.stack.pop()
        self.size -= 1
        if num == self.getMin():
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[self.size - 1]

    def getMin(self) -> int:
        return self.min_stack[-1]
        
