import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = [[(x[0] ** 2 + x[1] ** 2)] + x for x in points]
        heapq.heapify(points)
        
        sorted_list = []
        for _ in range(0, k):
            sorted_list.append(heapq.heappop(points))
        
        return [[x[1], x[2]] for x in sorted_list]