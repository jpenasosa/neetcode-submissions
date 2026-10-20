class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i, j = 0, 1

        while i < len(nums) - 1:
            # window size exceeds k; reset and shift
            if j == len(nums) or j - i > k:
                i += 1
                j = i + 1
            
            # Found a match
            elif nums[i] == nums[j]:
                return True
            
            # Grow the window
            else:
                j += 1
        
        return False
            

