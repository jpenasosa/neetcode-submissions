class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        cache = {}

        def validate(i, stack):
            args = (i,stack)
            if args in cache:
                return cache[args]

            if stack < 0: return False
            if i >= len(s): return not stack
            wildcard = False

            for j in range(i, n):
                c = s[j]
                if c == ")":
                    # exit early if stack becomes negatives
                    stack -= 1
                    if stack < 0:
                        break
                elif c == "(":
                    stack += 1
                else:
                    wildcard = True
                    break

            if wildcard:
                res = (
                    validate(j+1, stack+1)
                    or validate(j+1, stack-1)
                    or validate(j+1, stack)
                )
            else:
                res = not stack

            cache[args] = res
            return res

        ans = validate(0, 0)
        return ans