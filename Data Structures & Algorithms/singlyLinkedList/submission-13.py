class Node:
    def __init__(self, val, next_=None):
        self.val = val
        self.next = next_
    
    def __repr__(self):
        return f"Node(val={self.val})"

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.size = 0

    
    def get(self, index: int) -> int:
        curr = self.head
        i = 0
        while curr is not None and i < index:
            curr = curr.next
            i += 1
        
        if i == index and curr:
            return curr.val
        
        return -1

    def insertHead(self, val: int) -> None:
        self.head = Node(val, self.head)
        if self.tail is None:
            self.tail = self.head
        
        self.size += 1
        

    def insertTail(self, val: int) -> None:
        tail = Node(val)
        if self.head is None:
            self.head = self.tail = tail
            self.size += 1
            return

        self.tail.next = tail
        self.tail = self.tail.next
        self.size += 1


    def remove(self, index: int) -> bool:
        if index >= self.size:
            return False
        
        if index == 0:
            self.head = self.head.next
        else:
            curr = self.head
            i = 1
            while i < index and curr:
                curr = curr.next
                i += 1

            if curr.next:
                if curr.next is self.tail:
                    self.tail = curr
                curr.next = curr.next.next

        # Update size, and set tail
        self.size -= 1
        if self.size == 0:
            # Empty list, set tail to None
            self.tail = None

        return True
        

    def getValues(self) -> List[int]:
        values = []
        curr = self.head
        while curr:
            values.append(curr.val)
            curr = curr.next

        return values
        
