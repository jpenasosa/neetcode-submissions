import itertools

class Solution:
    def XORTotal(self, ss: Tuple[int]) -> int:
        total = 0
        for n in ss:
            total ^= n
        
        return total

    def subsetXORSum(self, nums: List[int]) -> int:
        xor_sum = 0

        for k in range(1, len(nums) + 1):
            for comb in itertools.combinations(nums, k):
                xor_sum += self.XORTotal(comb)

        # Calculate sum of XOR totals
        return xor_sum
        