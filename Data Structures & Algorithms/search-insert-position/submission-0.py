class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        def _binary_search(left=0, right=len(nums)-1):
            
            if left > right:
                return right + 1
                
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            
            if nums[mid] > target:
                return _binary_search(left=left, right=mid-1)
            else:
                return _binary_search(left=mid+1, right=right)


        return _binary_search()