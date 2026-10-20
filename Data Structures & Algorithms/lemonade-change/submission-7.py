from collections import defaultdict

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        register = defaultdict(int)

        for bill in bills:
            register[bill] += 1
            change = bill - 5

            # Give change starting with 10s, using at most all the 10s in the register
            if register[10] and change > 10:
                register[10] -= 1
                change -= 10

            # Use 5s for the remainder of the change
            register[5] -= change // 5
            if register[5] < 0:
                return False

        return True
