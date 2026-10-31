class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        ans = set()

        pacific = set()
        atlantic = set()

        def dfs(row, col, prev_height, ocean_set):
            if (
                row not in range(ROWS)
                or col not in range(COLS)
                or (row, col) in ocean_set
                or heights[row][col] < prev_height
            ):
                return

            ocean_set.add((row, col))
            height = heights[row][col]

            dfs(row + 1, col, height, ocean_set)
            dfs(row - 1, col, height, ocean_set)
            dfs(row, col + 1, height, ocean_set)
            dfs(row, col - 1, height, ocean_set)

        # Pacific ocean (first row)
        for col in range(COLS):
            dfs(0, col, heights[0][col], pacific)
            dfs(ROWS - 1, col, heights[ROWS - 1][col], atlantic)

        # Pacific ocean (first col)
        for row in range(ROWS):
            dfs(row, 0, heights[row][0], pacific)
            dfs(row, COLS-1, heights[row][COLS-1], atlantic)

        ans.update(pacific & atlantic)
        return sorted(ans)
