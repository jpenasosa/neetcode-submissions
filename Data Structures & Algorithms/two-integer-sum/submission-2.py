class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Keep track of seen values, only retaining the first instance for duplicates
        seen = dict()
    
        for j, num in enumerate(nums):
            if (i := seen.get(target - num)) is not None:
                return [i, j]

            seen[num] = j
        
        raise ValueError("No answer")