class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n:
            n &= (n - 1)
            ans += 1
        
        return ans

    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            ones = 0
            while i:
                i &= (i-1)
                ones += 1
            
            ans.append(ones)
        
        return ans
        