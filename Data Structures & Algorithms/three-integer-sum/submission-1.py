class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()

        length = len(nums)
        seen = set()
        nums = sorted(nums)

        for k in range(length - 1, -1, -1):
            n3 = nums[k]

            i, j = 0, k - 1

            while i < j:
                n1, n2 = nums[i], nums[j]
                sum_ = n1 + n2 + n3

                if sum_ == 0:
                    ans.add((n1, n2, n3))
                    i += 1
                
                elif sum_ > 0:
                    j -= 1
                
                else:
                    i += 1

        return [list(tup) for tup in ans]
