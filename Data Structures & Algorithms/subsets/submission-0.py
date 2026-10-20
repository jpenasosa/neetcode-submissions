class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def dfs(i: int, path: List[int]):
            if i == len(nums):
                ans.append(path)
                return
            
            dfs(i + 1, path.copy())
            dfs(i + 1, path.copy() + [nums[i]])
        
        dfs(0, [])

        return ans
    