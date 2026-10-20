class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        land_nodes = set()

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == '1':
                    land_nodes.add((i,j))

        print(len(land_nodes), "pieces of land found")

        def dfs(row: int, col: int):
            if min(row, col) < 0 or row == ROWS or col == COLS or grid[row][col] == '0':
                return

            # Mark it as water so we don't come back
            land_nodes.discard((row,col))
            grid[row][col] = '0'

            dfs(row+1, col)
            dfs(row, col+1)
            dfs(row-1, col)
            dfs(row, col-1)

        count = 0
        while land_nodes:
            row, col = land_nodes.pop()
            dfs(row, col)
            count += 1

        return count
