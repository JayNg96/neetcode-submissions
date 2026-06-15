import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while len(stones) > 1:
            heapq._heapify_max(stones)
            temp_1 = heapq.heappop(stones)
            heapq._heapify_max(stones)
            temp_2 = heapq.heappop(stones)
            heapq.heappush(stones, abs(temp_1 - temp_2))

        return stones[0]