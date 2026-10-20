# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        lo, hi = 1, n
        while lo <= hi:
            pick = (lo+hi)//2
            res = guess(pick)
            if res == 0:
                return pick
            elif res < 0:
                hi = pick - 1
            else:
                lo = pick + 1
        
        return -1
