class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length = len(nums)

        ans = []
        for i in range(length - 2):
            # sum can only be 0 if at least the first number is negative
            if nums[i] > 0:
                break

            # prevent duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue

            j, k = i + 1, length - 1
            while j < k:
                summed = nums[i] + nums[j] + nums[k]
                if summed == 0:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1

                elif summed < 0:
                    j += 1
                else:
                    k -= 1

        return ans
