class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        lo, hi = 1, num

        while lo <= hi:
            n = (hi + lo)//2
            sq = n * n
            if sq == num:
                return True
            elif sq > num:
                hi = n - 1
            else:
                if hi * hi < num:
                    return False
                else:
                    lo = n + 1

        return False
