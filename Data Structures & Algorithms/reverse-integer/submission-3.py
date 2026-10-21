import math

class Solution:
    def reverse(self, x: int) -> int:
        MIN = -(1 << 31)
        MAX = 1 - MIN

        ans = 0
        while x:
            ans = ans * 10 + int(math.fmod(x, 10))
            x = int(x / 10)

        if ans < MIN or ans > MAX:
            return 0
        
        return ans
