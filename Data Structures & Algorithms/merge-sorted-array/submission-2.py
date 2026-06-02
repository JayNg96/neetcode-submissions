from typing import List
class Solution:

    def merge(self,nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        k = m+n-1
        i = k
        j = len(nums2) - 1
        if m != 0:
            while nums1[i] == 0:
                i-=1
        else:
            i = 0

        while k >= 0:
            if i >= 0 and j >= 0 and m!=0:
                if nums1[i] > nums2[j]:
                    nums1[k] = nums1[i]
                    i-=1
                else:
                    nums1[k] = nums2[j]
                    j-=1
            else:
                if j >= 0:
                    nums1[k] = nums2[j]
                    j-=1
                else:
                    break
            k-=1