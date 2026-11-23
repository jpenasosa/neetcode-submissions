from collections import defaultdict

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        summed = sum(nums)
        if abs(target) > summed:
            return 0

        m = 2 * summed + 1
        prev = [0]*m
        prev[summed] = 1

        cur = [0]*m

        for i in range(n):
            num = nums[i]
            for j in range(m):
                if not prev[j]:
                    continue

                cur[j - num] += prev[j]
                cur[j + num] += prev[j]

            cur, prev = [0]*m, cur

        return prev[summed+target]
