class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Calcuate the xor_total of the range first
        xor_total = 0
        for num in nums:
            xor_total ^= num
        
        # xor against all possibles in the range, all present values cancel out, leaving the missing number
        ans = xor_total
        for num in range(len(nums) + 1):
            ans ^= num
        
        return ans