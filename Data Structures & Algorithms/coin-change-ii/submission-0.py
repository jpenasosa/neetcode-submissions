class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        cache = {}

        def dfs(i, cur=0):
            args = (i, cur)
            if args in cache:
                return cache[args]

            if cur == amount:
                return 1
            
            if i >= len(coins) or cur > amount:
                return 0

            res = dfs(i, cur + coins[i]) + dfs(i + 1, cur)
            cache[args] = res
            return res

        return dfs(0)
