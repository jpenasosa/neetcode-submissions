class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        dp = [0]*len(nums)
        a, b, c = 0, nums[0], nums[1]
        for i in range(2, len(nums)):
            tmp = nums[i] + max(b, a)
            a, b, c = b, c, tmp

        return max(a, b, c)
