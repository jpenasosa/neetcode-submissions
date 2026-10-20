from collections import defaultdict

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        register = defaultdict(int)

        for bill in bills:
            register[bill] += 1
            change = bill - 5

            # Give change starting with 10s, using at most all the 10s in the register
            n = min(register[10], change // 10)
            register[10] -= n
            change -= n * 10

            # Use 5s for the remainder of the change
            register[5] -= change // 5
            if register[5] < 0:
                return False

        return True
