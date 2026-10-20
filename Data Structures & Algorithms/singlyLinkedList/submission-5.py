class Node:
    def __init__(self, val, next_=None):
        self.val = val
        self.next = next_
    
    def __repr__(self):
        return f"Node(val={self.val})"

class LinkedList:
    
    def __init__(self):
        self.head = None

    
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
        

    def insertTail(self, val: int) -> None:
        tail = Node(val)

        if self.head is None:
            self.head = tail
            return

        curr = self.head
        while curr.next:
            curr = curr.next
        
        curr.next = tail


    def remove(self, index: int) -> bool:
        if index == 0:
            if self.head:
                self.head = self.head.next
                return True
            return False

        curr = self.head
        i = 1
        while curr and i < index:
            curr = curr.next
            i += 1

        if i == index and curr and curr.next:
            curr.next = curr.next.next
            return True
        
        return False
        

    def getValues(self) -> List[int]:
        values = []
        curr = self.head
        while curr:
            values.append(curr.val)
            curr = curr.next

        return values
        
