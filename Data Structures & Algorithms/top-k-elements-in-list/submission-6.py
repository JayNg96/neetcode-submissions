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

        for key, val in hash_map.items():        
            li.append((val, key))

        heapq.heapify(li)
        while len(li) > k:
            heapq.heappop(li)

        return [x[1] for x in li]

            


        