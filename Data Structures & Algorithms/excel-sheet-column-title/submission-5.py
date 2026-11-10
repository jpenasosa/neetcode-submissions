import string

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        chars = string.ascii_uppercase
        label = ''

        while columnNumber:
            columnNumber -= 1
            label += chars[columnNumber % 26]
            columnNumber //= 26
        
        return label[::-1]