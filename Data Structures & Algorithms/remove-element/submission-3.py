class Solution:
    # nums = [0,1,2,2,3,0,4,2]
    # target = 2
    # iter 3: [0,1,2,2,3,0,4,2]
    # iter 2: [2, 3, 2, 3]
    # iter 2: [2, 2, 3, 3]

    def removeElement(self, nums: List[int], val: int) -> int:
        end = len(nums) - 1
        i = 0

        while i <= end:
            if nums[i] == val:                
                # swap
                nums[i], nums[end] = nums[end], nums[i]
                end -= 1
            else:
                i += 1
        
        return end + 1