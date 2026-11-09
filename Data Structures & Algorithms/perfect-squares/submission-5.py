class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[1] = 1
        squares = []

        for i in range(2, n+1):
            # add perfect squares ahead of time
            sq = i * i
            if sq == n:
                return 1

            if sq < n:
                dp[sq] = 1
                squares.append(sq)
            
            # don't do need to do any work if perfect square
            if dp[i] > 0:
                continue

            dp[i] = i # worst case, sum of 1s
            for sq in squares:
                if sq > i:
                    break

                dp[i] = min(dp[i], dp[sq] + dp[i-sq])

        return dp[n]