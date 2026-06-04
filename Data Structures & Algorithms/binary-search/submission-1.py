class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def _binary_search(left:int , right:int) -> int:
            if left > right:
                return -1
            mid = ( right + left ) // 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                return _binary_search(left=mid+1, right=right)
            else:
                return _binary_search(left=left, right=mid-1)
            
        return _binary_search(left=0, right=len(nums)-1)