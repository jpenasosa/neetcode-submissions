class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr = 0

        i = j = 0
        while j < len(nums):
            curr += nums[j]
            max_sum = max(max_sum, curr)

            if curr < 0:
                i = j + 1
                curr = 0
            
            j += 1
            
        return max_sum
