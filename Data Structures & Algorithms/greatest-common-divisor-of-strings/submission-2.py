class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        length1 = len(str1)
        length2 = len(str2)

        x = ""
        for i in range(length2):
            substr = str2[:i+1]
            if substr * int(length2/(i+1)) == str2 and substr * int(length1/(i+1)) == str1:
                x = substr
        
        return x