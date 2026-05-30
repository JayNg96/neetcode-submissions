from collections import Counter

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return max(Counter(nums).values())>1 if nums else False