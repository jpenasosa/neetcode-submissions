import math

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        bor = 0
        for n in nums:
            bor |= n

        return bor * 1 << (len(nums) - 1)
