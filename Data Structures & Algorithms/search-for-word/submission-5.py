class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(row, col, path):
            idx = len(path)
            if idx == len(word):
                return True

            if min(row, col) < 0 or row >= rows or col >= cols or board[row][col] != word[idx] or (row, col) in path:
                return False
            
            path.add((row, col))

            exists = (
                dfs(row+1, col, path)
                or dfs(row-1, col, path)
                or dfs(row, col+1, path)
                or dfs(row, col-1, path)
            )
            path.discard((row, col))
            return exists

        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, path=set()):
                    return True
        
        return False