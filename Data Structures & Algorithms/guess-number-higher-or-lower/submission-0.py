# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        def _guess(left:int, right:int):
            mid = (left + right) // 2
            if guess(mid) == 0:
                return mid
            elif guess(mid) == -1: # guess is higher than n
                return _guess(left=left, right=mid-1)
            else:                  # guess is smaller than n
                return _guess(left=mid+1, right=right)
        return _guess(1, n)


        