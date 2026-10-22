class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1

        for i in range(len(digits) -1, -1, -1):
            if not carry:
                break

            num = digits[i] + 1
            digits[i] = num % 10
            carry = num // 10

        if carry:
            return [1] + digits

        return digits
