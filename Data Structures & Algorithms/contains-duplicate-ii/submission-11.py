class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0 or len(nums) <= 1:
            return False

        seen = set(nums[:k+1])
        if len(seen) <= k:
            return True

        i = k+1
        while i < len(nums):
            seen.remove(nums[i-k-1])

            if nums[i] in seen:
                return True

            seen.add(nums[i])
            i += 1

        return False

