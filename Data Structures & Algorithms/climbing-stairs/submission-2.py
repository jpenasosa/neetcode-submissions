class Solution:
    def climbStairs(self, n: int) -> int:
        # f(1) = 1
        # f(2) = 1 + f(1)
        # f(3) = f(2) + f(1)
        # ...
        # f(n) = f(n-2) + f(n-1)

        if n == 1:
            return 1

        a, b = 1, 1
        while n > 1:
            a, b = b, a + b
            n -= 1
        
        return b