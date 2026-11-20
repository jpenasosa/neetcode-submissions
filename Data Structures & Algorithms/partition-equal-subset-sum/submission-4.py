class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        
        n = len(nums)
        target = total//2
        dp = [[False]*(target+1) for _ in range(n)]

        dp[0] = [False if t < nums[0] else True for t in range(target+1)]
        for i in range(n):
            dp[i][0] = True

        for i in range(n):
            for t in range(target+1):
                dp[i][t] = dp[i-1][t]  # Skip current num
                if not dp[i][t] and t >= nums[i]:
                    dp[i][t] = dp[i-1][t-nums[i]]

        return dp[-1][target]