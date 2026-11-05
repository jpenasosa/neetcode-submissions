class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n, m = len(matrix), len(matrix[0])
        rows = [False]*n
        cols = [False]*m

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    rows[i] = True
                    cols[j] = True
        
        # Set rows with zeroes
        for i in range(n):
            if rows[i]:
                matrix[i] = [0]*m

        # Set columns with zeroes
        for j in range(m):
            for i in range(n):
                if cols[j]:
                    matrix[i][j] = 0