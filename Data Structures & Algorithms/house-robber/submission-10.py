class Solution:
    def rob(self, nums: List[int]) -> int:
        nums.append(0)
        for i in range(2, len(nums)):
            nums[i] = nums[i] + max(nums[i-2], nums[i-3])

        return max(nums[-2:])
