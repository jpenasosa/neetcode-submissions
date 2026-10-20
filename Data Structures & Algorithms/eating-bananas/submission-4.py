class Solution:
    def kokoEats(self, piles: List[int], h: int, k: int) -> bool:
        turn = 0
        for i in range(len(piles)):
            turns = piles[i]//k + (piles[i]%k != 0)
            turn += turns

        return turn <= h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h == len(piles):
            return max(piles)

        piles.sort()
        lo = 1
        hi = 2 * sum(piles) // h

        while lo + 1 < hi:
            mid = (lo + hi)//2
            eats = self.kokoEats(piles, h, mid)
            if not eats:
                lo = mid + 1
            else:
                hi = mid

        return lo if self.kokoEats(piles, h, lo) else hi
