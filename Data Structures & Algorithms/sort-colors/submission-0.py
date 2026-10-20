class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Count occurence of each color
        colors = [0,0,0]
        for color in nums:
            colors[color] += 1
        
        # Build output array
        i = 0
        for color, count in enumerate(colors):
            for _ in range(count):
                nums[i] = color
                i += 1

        return nums
        