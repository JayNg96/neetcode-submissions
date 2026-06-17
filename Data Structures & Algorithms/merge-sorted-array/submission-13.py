class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        def recur(num1_fullList_pointer, num1_validList_pointer, num2_validList_pointer):
            if num2_validList_pointer == -1:
                return
            
            if num1_validList_pointer != -1 and nums1[num1_validList_pointer] > nums2[num2_validList_pointer]:
                nums1[num1_fullList_pointer] = nums1[num1_validList_pointer]
                recur(num1_fullList_pointer-1, num1_validList_pointer-1, num2_validList_pointer)
            else:
                nums1[num1_fullList_pointer] = nums2[num2_validList_pointer]
                recur(num1_fullList_pointer-1, num1_validList_pointer, num2_validList_pointer-1)

        recur(num1_fullList_pointer=m+n-1, num1_validList_pointer=m-1, num2_validList_pointer=n-1)