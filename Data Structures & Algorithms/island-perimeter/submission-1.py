class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(row: int, col: int, visited: Set[Tuple[int, int]]) -> int:
            if (row, col) in visited:
                return 0

            if min(row, col) <0 or row == ROWS or col == COLS or grid[row][col] == 0:
                return 1

            # Move right and down
            visited.add((row, col))
            return (
                dfs(row + 1, col, visited)
                + dfs(row, col+1, visited)
                + dfs(row - 1, col, visited)
                + dfs(row, col-1, visited)
            )

        # Find a starting point
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    break

            # Exit if inner loop breaks
            else:
                continue
            break

        perimeter = dfs(row, col, set())
        return perimeter