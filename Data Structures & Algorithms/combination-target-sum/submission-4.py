class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        ans = []
        def dfs(i, total, path):
            if i == len(nums) or total > target:
                return
            
            if total == target:
                ans.append(path.copy())
                return

            # Do not include the i-th number
            dfs(i+1, total, path)

            # Include the i-th number
            num = nums[i]
            path.append(num)
            dfs(i, total + num, path)
            path.pop()

        dfs(0, 0, [])
        return ans