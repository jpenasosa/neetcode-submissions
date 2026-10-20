class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alphabet = dict(zip(order, range(len(order))))
        alphabet[""] = -1

        values = []
        for word in words:
            value = tuple(alphabet[c] for c in word)
            values.append(value)
        
        return values == sorted(values)
