class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        length = len(nums)
        nums.sort()

        for i in range(length):
            j, k = i + 1, length - 1
            while j < k:
                summed = nums[i] + nums[j] + nums[k]
                if summed == 0:
                    ans.add((nums[i], nums[j], nums[k]))
                    j += 1
                elif summed < 0:
                    j += 1
                else:
                    k -= 1

        return [list(trip) for trip in ans]
