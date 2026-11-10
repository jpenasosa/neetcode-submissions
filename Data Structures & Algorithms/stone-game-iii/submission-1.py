class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        cache = {}

        def dfs(i):
            if i in cache:
                return cache[i]

            if i >= len(stoneValue):
                return 0

            res = max(sum(stoneValue[i:i+n]) - dfs(i+n) for n in (1, 2, 3))
            cache[i] = res
            return res

        points = dfs(0)
        if points > 0:
            return "Alice"
        elif points < 0:
            return "Bob"        
        return "Tie"
