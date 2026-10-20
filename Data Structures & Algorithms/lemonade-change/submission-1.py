from collections import defaultdict

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        register = defaultdict(int)
        values = [10, 5]

        for bill in bills:
            register[bill] += 1
            change = bill - 5

            for val in values:
                if change >= val and register[val]:
                    count = change // val
                    register[val] -= count
                    change -= val * count

            if change or any(val<0 for val in register.values()):
                return False

        return True
