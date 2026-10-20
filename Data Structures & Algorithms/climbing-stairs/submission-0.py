class Solution:
    def climbStairs(self, n: int) -> int:
        # f(n) = f(n - 1) + f(n - 2)
        # f(3) = f(2) + f(1)
        # f(2) = 2
        # f(1) = 1
        # f(0) = 0
        
        if n < 3:
            return n
        
        a ,b = 1, 2
        for i in range(3, n+1):
            temp = a
            a = b
            b = b + temp

        return b