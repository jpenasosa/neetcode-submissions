class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n, m = len(matrix), len(matrix[0])
        top_zero = False

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    if i > 0:
                        matrix[i][0] = 0
                    else:
                        top_zero = True

        # Set columns with zeroes
        for i in range(n-1, 0, -1):
            for j in range(m-1, -1, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if top_zero:
            matrix[0] = [0]*m
            return
