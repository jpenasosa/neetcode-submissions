class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        ans = int(str(x)[::-1])

        if sign == -1 and ans > (1 << 31):
            return 0
        elif ans > (1 << 31) - 1:
            return 0
        
        return ans * sign
