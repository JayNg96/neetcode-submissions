from collections import Counter
from itertools import islice

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return list(dict(islice(Counter(nums).most_common(), k)))