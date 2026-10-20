class MyQueue:

    def __init__(self):
        self.stack = []
        self.staq = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if self.staq:
            return self.staq.pop()

        for _ in range(len(self.stack) - 1):
            self.staq.append(self.stack.pop())
        
        return self.stack.pop()

    def peek(self) -> int:
        value = self.pop()
        self.staq.append(value)
        return value

    def empty(self) -> bool:
        return not self.stack and not self.staq


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()