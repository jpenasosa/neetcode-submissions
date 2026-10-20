class Solution:
    def isValid(self, s: str) -> bool:
        unmatched = []
        end = len(s)
        matches = {"(":")", "[":"]", "{":"}"}

        for char in s:
            if char not in "()[]{}":
                return False

            if char in matches:
                unmatched.append(char)
                continue
            elif unmatched and matches[unmatched[-1]] == char:
                    unmatched.pop()
            else:
                return False
                
        
        return not unmatched

            




        