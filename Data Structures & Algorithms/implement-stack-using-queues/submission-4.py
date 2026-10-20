class MyStack:

    def __init__(self):
        self._top: int | None = None
        self.q = []

    def push(self, x: int) -> None:
        if self._top:
            self.q.append(self._top)

        self._top = x

    def pop(self) -> int:
        val = self._top
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.pop(0))

        self._top = self.q.pop(0) if self.q else None
        return val

    def top(self) -> int:
        return self._top

    def empty(self) -> bool:
        return len(self.q) == 0 and self._top is None


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()