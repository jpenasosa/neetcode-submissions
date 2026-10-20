class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        nums = sorted(nums)
        length = len(nums)

        print(nums)

        for a in range(length - 3):
            num_a = nums[a]
            if a > 0 and num_a == nums[a-1]:
                a += 1
                continue

            for b in range(a+1, length - 2):
                num_b = nums[b]
                if b > a + 1 and num_b == nums[b-1]:
                    b += 1
                    continue
            
                c = b + 1
                d = length - 1

                while c < d:
                    if c > b + 1 and nums[c] == nums[c-1]:
                        c += 1
                        continue

                    num_c, num_d = nums[c], nums[d]
                    sum_ = num_a + num_b + num_c + num_d

                    if sum_ == target:
                        ans.append([num_a, num_b, num_c, num_d])
                        c += 1
                    
                    elif sum_ > target:
                        d -= 1
                    
                    else:
                        c += 1

        return ans