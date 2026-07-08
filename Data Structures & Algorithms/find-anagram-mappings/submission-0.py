class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        nums_dict = {y: x for x, y in enumerate(nums2)}
        
        idx_li = []

        for n in nums1:
            idx_li.append(nums_dict[n])

        return idx_li
