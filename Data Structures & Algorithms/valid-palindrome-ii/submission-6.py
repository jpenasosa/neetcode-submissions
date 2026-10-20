class Solution:
    def isPalindrome(self, s: str, l: int, r: int, deleted: bool = False) -> bool:
        if l >= r:
            return True

        if s[l] != s[r]:
            if deleted:
                return False

            return self.isPalindrome(s, l + 1, r, deleted=True) or self.isPalindrome(s, l, r - 1, deleted=True)
        
        return self.isPalindrome(s, l + 1, r - 1, deleted)

    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        result = self.isPalindrome(s, l, r)
        return result