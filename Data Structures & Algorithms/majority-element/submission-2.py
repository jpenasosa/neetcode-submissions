from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elm, max_count = -1, 0

        for num in nums:
            if num != elm:
                if max_count <= 0:
                    elm = num
                    max_count = 1
                else:
                    max_count -= 1
            else:
                max_count += 1
        
        return elm