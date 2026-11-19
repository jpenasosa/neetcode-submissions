class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]

        max_cur, min_cur = 1, 1
        for num in nums:
            tmp = max(max_cur*num, min_cur*num, num)
            min_cur = min(min_cur*num, max_cur*num, num)
            max_cur = tmp

            ans = max(ans, max_cur)
        
        return ans
