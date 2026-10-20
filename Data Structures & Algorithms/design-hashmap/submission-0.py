class MyHashMap:
    capacity: int = 7919

    def __init__(self):
        self.arr = [None] * self.capacity
        
    @classmethod
    def _hash(cls, key: int) -> int:
        return key % cls.capacity

    def put(self, key: int, value: int) -> None:
        hash_ = self._hash(key)
        self.arr[hash_] = value

    def get(self, key: int) -> int:
        hash_ = self._hash(key)
        value = self.arr[hash_]
        return value if value is not None else -1

    def remove(self, key: int) -> None:
        hash_ = self._hash(key)
        self.arr[hash_] = None
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)