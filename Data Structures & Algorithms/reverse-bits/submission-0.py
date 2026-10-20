class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        digit = 1 << 31

        for i in range(32):
            if n & (1 << i):
                ans += digit
            digit >>= 1

        return ans
