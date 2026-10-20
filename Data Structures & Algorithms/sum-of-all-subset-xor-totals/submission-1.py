class Solution:
    def XORTotal(self, ss: List[int]) -> int:
        total = 0
        for n in ss:
            total ^= n
        
        return total

    def subsetXORSum(self, nums: List[int]) -> int:
        subsets = []

        # Append subsets of nums
        def buildSubsets(i: int, path: List[int]):
            if i >= len(nums):
                return

            # Build a subset which excludes the current number
            buildSubsets(i+1, path.copy())

            path.append(nums[i])
            subsets.append(path)
            buildSubsets(i+1, path.copy())

        # Accumulate subsets
        buildSubsets(0, [])

        # Calculate sum of XOR totals
        return sum(self.XORTotal(ss) for ss in subsets)
        