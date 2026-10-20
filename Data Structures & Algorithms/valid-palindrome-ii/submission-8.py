class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                skip_left = s[l+1:r+1]
                if skip_left == skip_left[::-1]:
                    return True
                
                skip_right = s[l:r]
                if skip_right == skip_right[::-1]:
                    return True
                
                return False

            l += 1
            r -= 1

        return True