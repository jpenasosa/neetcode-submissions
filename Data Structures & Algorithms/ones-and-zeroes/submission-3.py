# Completed using bottom-up Solution
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        L = len(strs)
        counts = []

        for string in strs:
            zeroes, ones = 0, 0
            for c in string:
                if c == "0":
                    zeroes += 1
                else:
                    ones += 1

            counts.append((zeroes, ones))

        dp = [ [[0]*(n+1) for _ in range(m+1)] for _ in range(L+1) ]

        for i in range(1, L+1):
            mi, ni = counts[i-1]
            for j in range(m+1):
                for k in range(n+1):
                    res = dp[i-1][j][k]
                    if j >= mi and k >= ni:
                        res = max(res, 1 + dp[i - 1][j - mi][k - ni])

                    dp[i][j][k] = res

        return dp[-1][m][n]
