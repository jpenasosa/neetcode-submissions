class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        max_area = 0

        def dfs(row, col):
            if min(row, col) < 0 or row == rows or col == cols or grid[row][col] == 0:
                return 0

            grid[row][col] = 0
            area = 1
            for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
                r, c = row+dr, col+dc
                area += dfs(r, c)
            
            return area
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    max_area = max(max_area, dfs(i, j))
        
        return max_area
