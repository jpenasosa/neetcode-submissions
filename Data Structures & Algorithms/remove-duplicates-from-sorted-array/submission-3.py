class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        i = k = 0

        while i < len(nums):
            if nums[i] not in seen:
                seen.add(nums[i])
                nums[k] = nums[i]
                k += 1

            i += 1

        return k
        