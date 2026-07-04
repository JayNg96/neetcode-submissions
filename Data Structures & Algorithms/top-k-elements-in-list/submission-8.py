import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        hash_map = {}
        
        for n in nums:
            if n not in hash_map:
                hash_map[n] = 1
            else:
                hash_map[n] += 1
            
        
        li = []

        for num, count in hash_map.items():        
            heapq.heappush(li, (count, num))
            if len(li) > k:
                heapq.heappop(li)
        print(li)
        return [x[1] for x in li]
            


        