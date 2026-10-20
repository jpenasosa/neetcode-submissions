class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # idea, perform binary search twice. First finds the row, second finds the target
        bot, top = 0, len(matrix) - 1
        while bot < top:
            mid = (bot + top)//2
            pick = matrix[mid][-1]
            if pick == target:
                return True
            elif pick < target:
                bot = mid + 1
            else:
                top = mid - 1
        
        # Quick check to ensure target is in the row
        row = matrix[bot]
        print(f"Searching row={bot}: ", row, bot, top)
        if target < row[0]:
            return False
        if target > row[-1] and bot + 1 < len(matrix):
            row = matrix[bot + 1]

        # Typical binary search
        lo, hi = 0, len(row) - 1
        while lo <= hi:
            mid = (lo + hi)//2
            if row[mid] == target:
                return True
            elif row[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1

        return False