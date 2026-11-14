# F(0)= nums[0]
# F(1) = max(nums[0], nums[1])
# F(2) = max(nums[0] + nums[2], nums[1])
# F(3) = max(nums[0] + nums[2], nums[1] + nums[3], nums[0] + nums[3])
#      = max(nums[3] + max(nums[0] + nums[1]), nums[0] + nums[2])
#      = max(nums[3] + F(1), F(2))

class Solution:

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 3:
            return max(nums)

        def _rob(start, stop):
            a, b, c = 0, nums[start], nums[start+1]
            for i in range(start+2, stop):
                a, b, c = b, c, nums[i] + max(a, b)

            return max(b, c)

        return max(_rob(1, n), _rob(0, n-1))
