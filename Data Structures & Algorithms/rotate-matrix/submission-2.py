class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        if n <= 1:
            return

        for k in range(n//2):
            lo, hi = k, n-1-k

            top = matrix[lo][lo:hi+1].copy()
            bot = matrix[hi][lo:hi+1].copy()
            left = [matrix[i][lo] for i in range(hi-1, lo, -1)]
            right = [matrix[i][hi] for i in range(hi-1, lo, -1)]

            # Set right and left from top and down, respectively
            for i in range(lo, hi+1):
                matrix[i][lo] = bot[i-lo]
                matrix[i][hi] = top[i-lo]

            # Assign top from left, and bot from right
            matrix[lo][lo+1:hi] = left
            matrix[hi][lo+1:hi] = right
