class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        i, j = 0, 0

        while j < len(nums):
            if len(seen) > k:
                seen.remove(nums[i])
                i += 1

            if nums[j] in seen:
                return True

            seen.add(nums[j])
            j += 1

        return False

