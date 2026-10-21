class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left == right:
            return right
        
        ans = 0
        digit = 1
        rng = right - left

        while digit <= left:
            if not left & digit:
                digit <<= 1
                continue

            if rng < (digit << 1) - (left % (digit << 1)):
                ans |= digit 

            digit <<= 1

        return ans
