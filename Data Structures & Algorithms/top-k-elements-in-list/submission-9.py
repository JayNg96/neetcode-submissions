import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        hash_map = {}
        
        for n in nums:
            hash_map[n] = 1 + hash_map.get(n, 0)
            
        
        li = []
        for num, count in hash_map.items():        
            heapq.heappush(li, (count, num))
            if len(li) > k:
                heapq.heappop(li)

        return [x[1] for x in li]
            


        