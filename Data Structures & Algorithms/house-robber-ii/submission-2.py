"""
F(0) = nums[0]
F(1) = max(nums[0], nums[1])
F(2) = max(nums[0], nums[1], nums[2])
F(3) = max(nums[1] + nums[3], nums[0] + nums[2])
F(4) = max(nums[0] + nums[2], nums[1] + nums[3], nums[0] + nums[3], nums[1] + nums[4], nums[2] + nums[4])
     = max(F(3), nums[0] + nums[3], nums[1] + nums[4], nums[2] + nums[4])
     = max(nums[4] + max(nums[2], nums[1]), nums[3] + max(nums[1], nums[0]), nums[0] + nums[2])
     = max(nums[0] + max(nums[2], nums[3]), nums[1] + max(nums[3], nums[4]), nums[2] + nums[4])
F(5) = max(nums[0,2,4], nums[1,3,5], nums[0,3], nums[1,4], nums[2,5])
     = max(nums[0] + max(nums[2,4], nums[3]), nums[1] + max(nums[3,5], nums[4]), nums[2,5])
     = max(nums[])
"""

class Solution:
    def rob1(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(rob2, n + rob1)
            rob1 = rob2
            rob2 = temp

        return rob2

    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)

        return max(self.rob1(nums[:-1]), self.rob1(nums[1:]))
