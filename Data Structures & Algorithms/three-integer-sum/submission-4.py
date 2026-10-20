class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []

        length = len(nums)
        seen = set()
        nums = sorted(nums)

        for i in range(length - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            n1 = nums[i]
            j, k = i + 1, length - 1

            while j < k:
                if j > i + 1 and nums[j] == nums[j-1]:
                    j += 1
                    continue

                n2, n3 = nums[j], nums[k]
                sum_ = n1 + n2 + n3

                if sum_ == 0:
                    ans.append([n1, n2, n3])
                    j += 1
                
                elif sum_ > 0:
                    k -= 1
                
                else:
                    j += 1

        return ans
