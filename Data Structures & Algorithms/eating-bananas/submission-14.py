import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        total = sum(piles)
        lo, hi = 1, int(total + 1 / min(piles))

        def eat(k) -> bool:
            i = 0
            hours = 0

            for i in range(n):
                if hours > h:
                    return False

                hours += math.ceil(piles[i] / k)

            return hours <= h

        while lo < hi:
            k = (lo+hi)//2
            if eat(k):
                hi = k
            else:
                lo = k + 1

        return lo