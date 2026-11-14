# F(0)= nums[0]
# F(1) = max(nums[0], nums[1])
# F(2) = max(nums[0] + nums[2], nums[1])
# F(3) = max(nums[0] + nums[2], nums[1] + nums[3], nums[0] + nums[3])
#      = max(nums[3] + max(nums[0] + nums[1]), nums[0] + nums[2])
#      = max(nums[3] + F(1), F(2))

class Solution:
    def _rob(self, nums):
        a, b, c = 0, nums[0], nums[1]
        for i in range(2, len(nums)):
            a, b, c = b, c, nums[i] + max(a, b)

        return max(b, c)

    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        return max(self._rob(nums[1:]), self._rob(nums[:-1]))