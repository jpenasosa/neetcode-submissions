class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.arr = [None] * capacity
        self.size = 0

    def insert(self, key: int, value: int) -> None:
        idx = key % self.capacity
        curr = self.arr[idx]

        if curr is None:
            self.arr[idx] = Node(key, value)
            self.size += 1
        else:
            prev = None
            while curr:
                # If we find the same key, overwrite the value
                if curr.key == key:
                    curr.value = value
                    return

                prev, curr = curr, curr.next


            prev.next = Node(key, value)
            self.size += 1

        # Resize at 50% full
        if self.size >= self.capacity // 2:
            self.resize()

    def get(self, key: int) -> int:
        idx = key % self.capacity
        curr = self.arr[idx]
        
        while curr:
            if curr.key == key:
                return curr.value
            curr = curr.next
        
        return -1

    def remove(self, key: int) -> bool:
        idx = key % self.capacity
        curr = self.arr[idx]
        prev = None
        while curr:
            if curr.key == key:
                if prev:
                    prev.next = curr.next
                else:
                    self.arr[idx] = curr.next

                self.size -=1
                return True
            prev, curr = curr, curr.next
        return False


    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity


    def resize(self) -> None:
        # Double the array
        old = self.arr.copy()
        self.capacity *= 2
        self.size = 0
        self.arr = [None] * self.capacity

        # Re-calculate indexes
        for curr in old:            
            while curr:
                self.insert(curr.key, curr.value)
                curr = curr.next
            




