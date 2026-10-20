class Solution:
    def rob(self, nums: List[int]) -> int:
        # f(n) = max(nums[n] + f(n-2), f(n-1))
        # nums = [2,9,8,3,6]
        # f(5) = max(6 + f(3), f(4))
        # f(5) = max(6 + 8 + f(1), 3 + f(2))
        # f(5) = max(6+8+2, 3+9) = 16
        if len(nums) <= 2:
            return max(*nums, 0)

        n = len(nums) - 3
        while n >= 0:
            nums[n] += max(nums[n+2], nums[n+3] if n+3 < len(nums) else 0)
            n -= 1

        return max(nums[:2])
