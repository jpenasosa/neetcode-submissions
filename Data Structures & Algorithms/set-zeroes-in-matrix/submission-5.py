class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n, m = len(matrix), len(matrix[0])
        top_zero = False

        for j in range(m):
            if matrix[0][j] == 0:
                top_zero = True
                matrix[0][j] = True

        for i in range(1, n):
            for j in range(m):
                if matrix[i][j] == 0:
                    matrix[i][0] = True
                    matrix[0][j] = True

        # Set columns with zeroes
        for i in range(n-1, 0, -1):
            for j in range(m-1, -1, -1):
                if matrix[i][0] is True or matrix[0][j] is True:
                    matrix[i][j] = 0

        if top_zero:
            matrix[0] = [0]*m
            return
        
        for j in range(m):
            if matrix[0][j] is True:
                matrix[0][j] = 0

