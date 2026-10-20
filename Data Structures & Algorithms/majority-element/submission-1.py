from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elm, max_count = -1, 0
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1

            if (cnt := counts[num]) > max_count:
                elm = num
                max_count = cnt
        
        return elm