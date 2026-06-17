class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        # pointer should point to last item in list which is m + n - 1 <= assume this is k
        # then a pointer to last valid element of nums1 which is m - 1 <= assume this is i
        # and then a pointer to last element of nums2 which is n - 1   <= assume this is j
        # recursion method, initialize the parameter of k, i, j
        # then in the method, compare nums1[i] and nums2[j], 
        # assign the bigger value to nums[k] then move the pointer for either i or j forward
        # by recusively calling with i - 1 / j - 1 / and lastly k - 1 and ofcourse

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