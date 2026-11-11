class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total // 2
        n = len(nums)
        sums = set([0])

        for num in nums:
            for s in sums.copy():
                if s + num == target:
                    return True
                sums.add(num + s)

        return False
