class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        counts = [0, 0 ,0]
        for col in nums:
            counts[col] += 1
        
        i = 0
        for col, count in enumerate(counts):
            for _ in range(count):
                nums[i] = col
                i += 1
