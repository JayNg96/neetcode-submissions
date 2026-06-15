import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Python’s heapq module only implements a Min-Heap. 
        # To simulate a Max-Heap, the standard technique is to multiply all values by -1.
        stones = [-x for x in stones]
        heapq.heapify(stones)
        print(stones)
        
        while len(stones) > 1:
            largest = heapq.heappop(stones)
            second_largest = heapq.heappop(stones)
            heapq.heappush(stones, largest - second_largest)

        return -stones[0]