class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_w = 1
        bucket = [0]*101
        for w in stones:
            max_w = max(max_w, w)
            bucket[w] += 1
        
        w = max_w
        prev = 0
        while w > 0:
            if bucket[w] == 0:
                w -= 1
                continue

            if prev:
                diff = prev - w

                bucket[diff] += 1
                bucket[w] -= 1
                if diff > w:
                    w = diff
                    prev = 0
                    continue

            if bucket[w] % 2 == 0:
                prev = 0
            else:
                prev = w

            bucket[w] = 0
            w -= 1

        return prev
