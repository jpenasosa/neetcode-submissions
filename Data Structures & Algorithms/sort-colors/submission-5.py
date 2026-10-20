class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        i = 0
        lft = 0
        rht = len(nums) - 1

        while i <= rht:
            if nums[i] < 1:
                nums[i], nums[lft] = nums[lft], nums[i]
                i += 1
                lft += 1
            elif nums[i] > 1:
                nums[i], nums[rht] = nums[rht], nums[i]
                rht -= 1
            else:
                i += 1
