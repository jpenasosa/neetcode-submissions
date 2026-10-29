class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroes = 0
        product = 1
        for num in nums:
            if num == 0:
                zeroes += 1
            else:
                product *= num

        if zeroes > 1:
            return [0]*len(nums)

        if zeroes == 1:
            return [product if num==0 else 0 for num in nums]
        
        return [product//num for num in nums]