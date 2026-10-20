class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        xor_sum = 0

        # Append subsets of nums
        def buildSubsets(i: int, total: int = 0):
            if i == len(nums):
                return total

            # Build 2 subset, one excludes, other includes the current number
            return buildSubsets(i+1, total) + buildSubsets(i+1, total ^ nums[i])

        # Accumulate subsets
        return buildSubsets(0)
        