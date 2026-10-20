class Solution:
    def _binarySearch(self, nums: List[int], target: int) -> bool:
        print("binary search {target=}: ", nums)
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid            
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        bot, top = 0, len(matrix) - 1

        while bot <= top:
            mid = (top + bot)//2

            # Smaller than anything in mid row
            if target < matrix[mid][0]:
                top = mid - 1
            # Larger than anything in mid row
            elif target > matrix[mid][-1]:
                bot = mid + 1
            # Could only be in mid row
            else:
                bot = top = mid
                break

            print(f"{mid=}, {bot=}, {top=}")

        # mid = (top + bot)//2
        return self._binarySearch(matrix[mid], target) != -1