class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp_max = [0]*len(nums)
        dp_max[-1] = nums[-1]
        dp_min = dp_max.copy()

        for i in range(len(nums)-2, -1, -1):
            dp_max[i] = max(nums[i], nums[i]*dp_max[i+1], nums[i]*dp_min[i+1])
            dp_min[i] = min(nums[i], nums[i]*dp_max[i+1], nums[i]*dp_min[i+1])

        return max(dp_max)