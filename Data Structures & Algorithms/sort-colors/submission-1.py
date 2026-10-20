class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        counts = [0, 0 ,0]
        for col in nums:
            counts[col] += 1
        
        lo = 0
        for col in [0,1,2]:
            hi = lo + counts[col]
            for i in range(lo, hi):
                nums[i] = col

            lo = hi
