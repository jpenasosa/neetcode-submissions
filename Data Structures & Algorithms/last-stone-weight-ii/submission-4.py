class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        target = total // 2
        cache = {}

        def dfs(i, weight):
            if weight >= target or i == len(stones):
                return abs(weight - (total - weight))

            if (i ,weight) in cache:
                return cache[(i, weight)]
            
            res = min(dfs(i + 1, weight), dfs(i+1, weight + stones[i]))
            cache[(i, weight)] = res
            return res

        return dfs(0, 0)
