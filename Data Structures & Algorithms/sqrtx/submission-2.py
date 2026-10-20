class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x

        lo, hi = 1, x
        while lo + 1 < hi:
            mid = (lo + hi)//2
            sqr = mid * mid
            if sqr == x:
                return mid
            if sqr > x:
                hi = mid - 1
            else:
                lo = mid
        
        return lo if hi * hi > x else hi
