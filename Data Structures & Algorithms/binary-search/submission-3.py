class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def _binary_search(l, r):

            if l > r:
                return -1
            
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid

            if target > nums[mid]:
                return _binary_search(l=mid+1, r=r)

            return _binary_search(l=l, r=mid-1)

        return _binary_search(0, len(nums)-1)