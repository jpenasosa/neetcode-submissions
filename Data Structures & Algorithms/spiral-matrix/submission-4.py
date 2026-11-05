class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])

        res = []

        depth = min(rows, cols)//2
        k = 0
        while k < depth:
            res.extend(matrix[k][k:cols-k])
            res.extend([ matrix[i][cols-k-1] for i in range(k + 1, rows-k-1) ])
            res.extend(matrix[rows-1-k][k:cols-k][::-1])
            res.extend([ matrix[i][k] for i in range(rows-k-2, k, -1) ])
            k += 1
        
        # Add final line for odd/rectangular matrices
        n, m = rows - 2*k, cols - 2*k
        if n == 1:
            res.extend(matrix[k][k:k+m])
        elif m == 1:
            res.extend([ matrix[i][k] for i in range(k, k+n)])

        return res
