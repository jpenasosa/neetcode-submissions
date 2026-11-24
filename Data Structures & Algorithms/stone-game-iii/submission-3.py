class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        cache = {}

        def dfs(i):
            if i in cache:
                return cache[i]

            if i >= n:
                return 0

            res = max([ sum(stoneValue[i:k]) - dfs(k) for k in range(i+1, i+4) ])
            cache[i] = res
            return res

        score = dfs(0)
        if score == 0:
            return "Tie"
        return "Alice" if score > 0 else "Bob"