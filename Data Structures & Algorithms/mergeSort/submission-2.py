# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def merge(self, left: List[pair], right: List[pair]):
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i].key <= right[j].key:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
            

        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged

    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) <= 1:
            return pairs

        mid = len(pairs) // 2
        left = self.mergeSort(pairs[:mid])
        right = self.mergeSort(pairs[mid:])
        
        return self.merge(left, right)