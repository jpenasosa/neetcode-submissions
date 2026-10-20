class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = []
        match = {
            ")": "(",
            "]": "[",
            "}": "{",
        }

        for c in s:
            if stack and match.get(c) == stack[-1]:
                stack.pop()
            else:
                stack.append(c)
        
        return not bool(stack)
