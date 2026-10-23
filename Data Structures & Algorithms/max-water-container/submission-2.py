class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        max_volume = 0
        while i < j:
            h = min(heights[i], heights[j])
            max_volume = max(max_volume, h * (j - i))
            if heights[i] < heights[j]:
                i += 1
            else:
                j -=1
        
        return max_volume