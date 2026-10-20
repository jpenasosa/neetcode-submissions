from collections import deque

class MyStack:

    def __init__(self):
        self.q = deque()
        self.head = deque()

    def push(self, x: int) -> None:
        if not self.head:
            self.head.appendleft(x)
        else:
            prev = self.head.pop()
            self.head.appendleft(x)
            self.q.appendleft(prev)
            self.q.rotate(len(self.q) - 1)


    def pop(self) -> int:
        value = self.head.pop()
        if self.q:
            self.head.appendleft(self.q.pop())

        return value

    def top(self) -> int:
        return self.head[0]
        

    def empty(self) -> bool:
        return not self.head


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()