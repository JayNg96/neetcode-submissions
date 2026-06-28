class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        nums_length = len(nums)
        if nums_length % 2 == 1:
            mid = nums_length // 2
            return nums[mid]
        else:
            mid_1 = (nums_length - 1) // 2
            mid_2 = nums_length // 2
            return (nums[mid_2] + nums[mid_1]) / 2
