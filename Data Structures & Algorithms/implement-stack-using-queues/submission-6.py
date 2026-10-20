from collections import deque

class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.appendleft(x)
        self.q.rotate(len(self.q) - 1)


    def pop(self) -> int:
        return self.q.pop()

    def top(self) -> int:
        value = self.pop()
        self.push(value)
        return value
        

    def empty(self) -> bool:
        return not self.q


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()