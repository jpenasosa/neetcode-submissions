class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        target = total // 2
        cache = {}

        def dfs(i, cur):
            if (i, cur) in cache:
                return cache[(i, cur)]

            if i == len(stones) or cur >= target:
                return abs(total - 2*cur)
            
            res = min(dfs(i+1, cur+stones[i]), dfs(i+1, cur))
            cache[(i, cur)] = res
            return res

        return dfs(0, 0)