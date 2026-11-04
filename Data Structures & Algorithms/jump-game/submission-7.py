class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if all(n > 0 for n in nums):
            return True
        
        if nums[0] == 0 and len(nums) > 1:
            return False

        max_jump = max(nums)
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] == 0:
                for j in range(i, i - max_jump, -1):
                    if nums[j] > i-j:
                        break
                else:
                    return False


        return True