from math import ceil
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def _minEatingSpeed(left: int, right:int) -> int:    
            if left > right:
                return left
            mid = (left + right) // 2
            total_hours = 0
            for p in piles:
                total_hours += ceil(p / mid)
        
            if h >= total_hours:
                return _minEatingSpeed(left=left, right=mid-1)
            else:
                return _minEatingSpeed(left=mid+1, right=right)
           
        return _minEatingSpeed(left=1, right=max(piles))