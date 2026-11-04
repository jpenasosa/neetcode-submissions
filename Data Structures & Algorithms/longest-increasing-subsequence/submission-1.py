class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans = 1
        dp = [1]*len(nums)

        for i in range(len(nums)):
            length = max([1 + dp[k] for k in range(i) if nums[i] > nums[k]], default=1)
            dp[i] = length
            ans = max(ans, length)
    
        return ans
