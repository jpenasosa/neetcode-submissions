class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        res = ""

        # Pad zeros to the shorter of the two
        if len(a) > len(b):
            b = "0" * (len(a) - len(b)) + b
        if len(b) > len(a):
            a = "0" * (len(b) - len(a)) + a

        while a:
            if a[-1] == b[-1]:
                bit = "1" if carry else "0"
                carry = 1 if a[-1] == "1" else 0
            else:
                bit = "0" if carry else "1"

            res = bit + res
            a, b = a[:-1], b[:-1]


        if carry:
            res = "1" + res

        return res