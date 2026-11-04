class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False]*len(nums)
        dp[-1] = True
        
        for i in range(len(nums)-1, -1, -1):
            for j in range(i, i + nums[i] + 1):
                if j >= len(nums) or dp[j]:
                    dp[i] = True
                    break

        print(dp)
        return dp[0]