class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total // 2
        cache = {}

        def dfs(i, cur):
            if (i, cur) in cache:
                return cache[(i, cur)]

            if i == len(nums) or cur > target:
                return float("inf")
            
            if cur == target:
                return cur

            res = min(dfs(i+1, cur + nums[i]), dfs(i+1, cur))
            cache[(i, cur)] = res
            return res

        return dfs(0, 0) == target
