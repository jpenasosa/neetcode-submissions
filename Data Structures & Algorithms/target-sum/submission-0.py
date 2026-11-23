class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        cache = {}

        def dfs(i, target):
            args = (i, target)
            if args in cache:
                return cache[args]

            if i == len(nums):
                return int(target == 0)

            res = dfs(i+1, target - nums[i]) + dfs(i+1, target+nums[i])
            cache[args] = res
            return res

        return dfs(0, target)
