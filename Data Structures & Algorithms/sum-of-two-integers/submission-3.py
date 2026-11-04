class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF

        while b:
            carry = (a & b) << 1
            xor = (a ^ b) & mask
            a, b = xor, carry & mask

        return a if a <= max_int else ~(a ^ mask)