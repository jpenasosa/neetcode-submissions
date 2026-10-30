class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1

        while lo + 1 < hi:
            mid = (lo + hi)//2
            if nums[mid] == target:
                return mid

            # Left side is sorted
            if nums[lo] < nums[mid]:
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1

            # Right is sorted
            else:
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1


        if nums[lo] == target:
            return lo
        if nums[hi] == target:
            return hi
        
        return -1