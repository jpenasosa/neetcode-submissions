class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[1] = 1

        for i in range(2, n+1):
            # add perfect squares ahead of time
            sq = i * i
            if sq == n:
                return 1

            if sq < n:
                dp[sq] = 1
            
            # don't do need to do any work if perfect square
            if dp[i] > 0:
                continue

            dp[i] = n # worst case, n * 1 = n
            for j in range(1, i//2 + 1):
                dp[i] = min(dp[i], dp[j] + dp[i-j])

        return dp[n]