class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = None
        count = 0
        for num in nums:
            if ans == num:
                count += 1
            else:
                if count == 0:
                    ans = num
                    count = 1
                else:
                    count -= 1
        
        return ans
