class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        max_area = 0

        def dfs(row, col):
            if min(row, col) < 0 or row == rows or col == cols or grid[row][col] == 0:
                return 0

            grid[row][col] = 0
            return 1 + (
                dfs(row + 1, col)
                + dfs(row, col + 1)
                + dfs(row - 1, col)
                + dfs(row, col - 1)
            )

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    max_area = max(max_area, dfs(i, j))

        return max_area
