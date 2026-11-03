class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]
        dp_max = dp_min = 1

        for i in range(len(nums)):
            tmp = nums[i]*dp_max
            dp_max = max(nums[i], tmp, nums[i]*dp_min)
            dp_min = min(nums[i], tmp, nums[i]*dp_min)
            ans = max(ans, dp_max)

        return ans