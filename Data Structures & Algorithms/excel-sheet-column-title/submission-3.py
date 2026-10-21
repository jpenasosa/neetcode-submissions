import string

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        letters = string.ascii_uppercase
        ans = ""

        while columnNumber:
            columnNumber -= 1
            idx = columnNumber % 26
            ans = letters[idx] + ans
            columnNumber //= 26

        return ans
