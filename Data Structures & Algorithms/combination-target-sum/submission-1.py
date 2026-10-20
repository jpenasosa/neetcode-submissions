class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []

        def dfs(i: int, path: List[int], sum_: int = 0):
            if sum_ == target:
                ans.append(path)
                return

            if sum_ > target or i == len(nums):
                return

            # Skip current index
            dfs(i+1, path.copy(), sum_)

            # Use current index
            num = nums[i]
            dfs(i, path.copy() + [num], sum_ + num)

        dfs(0, [])

        return ans
    