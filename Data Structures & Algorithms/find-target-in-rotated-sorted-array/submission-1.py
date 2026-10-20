class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            mid = (lo + hi)//2
            num = nums[mid]

            # Guessed right
            if num == target:
                return mid

            # Guess is too small
            if num < target:
                # if mid is in rotated portion there's larger numbers on both sides
                if num < nums[lo]:
                    # If lo boundary is too large, check right
                    if nums[lo] > target:
                        lo = mid + 1
                    else:
                        hi = mid - 1

                else:
                    lo = mid + 1

            # Guess is too large
            else:
                # mid is in rotated portion -- everything > mid is also too large
                if num < nums[lo]:
                    hi = mid - 1
                else:
                    # There could be smaller numbers on either side
                    if nums[lo] > target:
                        lo = mid + 1
                    else:
                        hi = mid - 1
        
        return -1
