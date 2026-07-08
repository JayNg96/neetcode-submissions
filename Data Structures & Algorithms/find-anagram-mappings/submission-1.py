class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:

        nums_dict = {y: x for x, y in enumerate(nums2)}

        return [nums_dict[n] for n in nums1]
