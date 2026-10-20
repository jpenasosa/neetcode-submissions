class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            mid = (lo + hi)//2
            curr = nums[mid]
            if curr == target:
                return mid
            elif curr < target:
                lo = mid + 1
            else:
                hi = mid - 1
            

        return hi + 1