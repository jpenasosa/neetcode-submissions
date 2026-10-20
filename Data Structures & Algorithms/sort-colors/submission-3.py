class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # O(n) count instances of each color
        colors = [0, 0, 0]
        for i in range(len(nums)):
            col = nums[i]
            colors[col] += 1
        
        # O(k=3) updating array, constant time
        i = 0
        for col in [0, 1, 2]:
            cnt = colors[col]
            nums[i:i+cnt] = [col] * cnt
            i += cnt


        
        

