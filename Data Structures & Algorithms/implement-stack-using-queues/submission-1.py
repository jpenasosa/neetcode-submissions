class MyStack:

    def __init__(self):
        self.length = 0
        self.q1 = []
        self.q2 = []

    def push(self, x: int) -> None:
        if self.q1:
            val = self.q1.pop(0)
            self.q2.append(val)
            self.q1.append(x)
        else:
            self.q1.append(x)

    def pop(self) -> int:
        val = self.q1.pop(0)
        q2 = []
        for _ in range(len(self.q2) - 1):
            q2.append(self.q2.pop(0))
        
        self.q1 = self.q2.copy()
        self.q2 = q2

        return val

    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        return len(self.q1) + len(self.q2) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()