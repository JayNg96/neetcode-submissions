class Solution: 
    def search(self, nums: List[int], target: int) -> int:
        

        def _dfs(l, r):
            if l > r:
                return -1

            mid = ( l + r ) // 2

            if nums[mid] == target:
                return mid
            
            if nums[mid] >= nums[l]: 
                if nums[mid] > target >= nums[l]:
                    return _dfs(l=l, r=mid-1)
                else:
                    return _dfs(l=mid+1, r=r)
            else:
                if nums[mid] <= target < nums[l]:
                    return _dfs(l=mid+1, r=r)
                else:
                    return _dfs(l=l, r=mid-1)     

        return _dfs(l = 0, r = len(nums) - 1)