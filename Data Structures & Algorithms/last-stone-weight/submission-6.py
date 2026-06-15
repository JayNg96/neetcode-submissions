import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            largest = heapq.heappop(stones)
            second_largest = heapq.heappop(stones)
            stone_remains = largest - second_largest
            if stone_remains != 0:
                heapq.heappush(stones, largest - second_largest) 

        return -stones[0] if stones else 0