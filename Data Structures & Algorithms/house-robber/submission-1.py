class Solution:
    def rob(self, nums: List[int]) -> int:
        # f(n) = max(nums[n] + f(n-2), f(n-1))
        # nums = [2,9,8,3,6]
        # f(5) = max(6 + f(3), f(4))
        # f(5) = max(6 + 8 + f(1), 3 + f(2))
        # f(5) = max(6+8+2, 3+9) = 16

        loot = [-1] * len(nums)

        def steal(n: int):
            if n < 0:
                return 0

            if loot[n] >= 0:
                return loot[n]

            money = max(nums[n] + steal(n-2), steal(n-1))
            loot[n] = money
            return money

        return steal(len(nums) - 1)