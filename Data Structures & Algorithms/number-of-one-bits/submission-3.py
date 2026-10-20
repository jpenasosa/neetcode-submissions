class Solution:
    def hammingWeight(self, n: int) -> int:
        place = 1
        ones = 0

        while place <= n:
            if place & n == place:
                ones += 1
            
            place <<= 1
        
        return ones
