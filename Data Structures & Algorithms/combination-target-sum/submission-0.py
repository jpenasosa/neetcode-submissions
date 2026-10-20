class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []

        def dfs(i: int, path: List[int], sum_: int = 0):
            if sum_ == target:
                ans.append(path.copy())
                return

            if sum_ > target or i == len(nums):
                return

            num = nums[i]
            path.append(num)
            dfs(i, path, sum_ + num)
            path.pop()
            dfs(i+1, path, sum_)

        dfs(0, [])

        return ans
    