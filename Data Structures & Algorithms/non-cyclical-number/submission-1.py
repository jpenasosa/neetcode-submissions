class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n not in seen:
            seen.add(n)
            
            sqr_sum = 0
            while n:
                sqr_sum += (n%10)**2
                n //= 10

            n = sqr_sum
            if n == 1:
                return True
        
        return False
        
