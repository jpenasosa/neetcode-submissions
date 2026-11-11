class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        cache = {}

        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            if i > j:
                return 0

            res = max(piles[i] - dfs(i+1, j), piles[j] - dfs(i, j-1))
            cache[(i, j)] = res
            return res
        
        return dfs(0, n-1) > 0
