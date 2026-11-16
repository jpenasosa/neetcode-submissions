class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        stars = []

        for i in range(len(s)):
            c = s[i]
            if c == "(":
                stack.append(i)
            elif c == "*":
                stars.append(i)
            else:
                if not stack and not stars:
                    return False
                if stack:
                    stack.pop()
                else:
                    stars.pop()

        if len(stack) > len(stars):
            return False
        
        while stack:
            if stack.pop() > stars.pop():
                return False

        return True


