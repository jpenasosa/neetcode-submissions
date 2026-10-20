class MyHashSet:
    capacity: int = 7919

    def __init__(self):
        self.arr = [None] * self.capacity

    @classmethod
    def _hash(cls, key: int) -> int:
        return key % cls.capacity

    def add(self, key: int) -> None:
        self.arr[self._hash(key)] = True

    def remove(self, key: int) -> None:
        self.arr[self._hash(key)] = None

    def contains(self, key: int) -> bool:
        return bool(self.arr[self._hash(key)])
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)