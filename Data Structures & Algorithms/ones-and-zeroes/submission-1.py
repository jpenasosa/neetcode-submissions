class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        counts = []

        for string in strs:
            zeroes, ones = 0, 0
            for c in string:
                if c == "0":
                    zeroes += 1
                else:
                    ones += 1

            counts.append((zeroes, ones))

        cache = {}
        def dfs(i, m, n):
            args = (i, m, n)
            if args in cache:
                return cache[args]

            if i == len(strs):
                return 0

            res = dfs(i+1, m, n)
            mi, ni = counts[i]
            if m >= mi and n >= ni:
                res = max(1 + dfs(i + 1, m - mi, n - ni), res)

            cache[args] = res
            return res

        
        return dfs(0, m, n)
