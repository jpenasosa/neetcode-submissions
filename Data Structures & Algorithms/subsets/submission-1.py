class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def dfs(i: int, path: List[int]):
            if i == len(nums):
                ans.append(path.copy())
                return
            
            path.append(nums[i])
            dfs(i + 1, path)
            path.pop()
            dfs(i + 1, path)
        
        dfs(0, [])

        return ans
    