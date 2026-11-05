class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length = len(nums)

        ans = set()
        for i in range(length - 2):
            j = i + 1
            k = length - 1
            target = -nums[i]
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