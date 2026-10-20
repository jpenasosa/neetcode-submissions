class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        arr = []

        i = 0
        length = min(len(word1), len(word2))
        while i < length:
            arr.append(word1[i])
            arr.append(word2[i])
            i += 1
        
        arr.extend(word1[i:])
        arr.extend(word2[i:])
        return "".join(arr)
    