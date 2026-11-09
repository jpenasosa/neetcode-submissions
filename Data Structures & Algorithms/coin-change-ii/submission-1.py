class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        n = len(coins)

        prev = [0]*(amount+1)
        cur = [0]*(amount+1)
        cur[0] = 1

        for i in range(n):
            for j in range(1, amount+1):
                cur[j] += prev[j]
                if j - coins[i] >= 0:
                    cur[j] += cur[j - coins[i]]

        return cur[-1]
