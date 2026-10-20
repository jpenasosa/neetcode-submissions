class Node:
    def __init__(self, value: int, *, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

class Deque:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def isEmpty(self) -> bool:
        return self.size == 0        

    def append(self, value: int) -> None:
        self.tail = Node(value, prev=self.tail)
        if self.tail.prev:
            self.tail.prev.next = self.tail

        if self.head is None:
            self.head = self.tail
        
        self.size += 1

    def appendleft(self, value: int) -> None:
        self.head = Node(value, next=self.head)
        if self.head.next:
            self.head.next.prev = self.head

        if self.tail is None:
            self.tail = self.head
        
        self.size += 1

    def pop(self) -> int:
        if self.tail is None:
            return -1

        value = self.tail.value
        self.tail = self.tail.prev
        self.size -= 1

        if self.tail:
            self.tail.next = None

        if self.isEmpty():
            self.head = None

        return value

    def popleft(self) -> int:
        if self.head is None:
            return -1

        value = self.head.value
        self.head = self.head.next
        self.size -= 1

        if self.head:
            self.head.prev = None
        
        if self.isEmpty():
            self.tail = None
        
        return value

