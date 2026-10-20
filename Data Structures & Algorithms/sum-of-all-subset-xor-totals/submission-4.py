class Solution:
    def XORTotal(self, ss: List[int]) -> int:
        total = 0
        for n in ss:
            total ^= n
        
        return total

    def subsetXORSum(self, nums: List[int]) -> int:
        xor_sum = 0

        # Append subsets of nums
        def buildSubsets(i: int, total: int = 0):
            if i >= len(nums):
                nonlocal xor_sum
                xor_sum += total
                return

            # Build 2 subset, one excludes, other includes the current number
            buildSubsets(i+1, total)
            buildSubsets(i+1, total ^ nums[i])

        # Accumulate subsets
        buildSubsets(0)

        # Calculate sum of XOR totals
        return xor_sum
        