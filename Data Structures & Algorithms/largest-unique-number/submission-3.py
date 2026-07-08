class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        nums.sort()
        l = len(nums) - 1
        r = len(nums) - 2

        while l >= 0:
            if nums[l] == nums[r]:
                l -= 2
                r -= 2
            else:
                return nums[l]
        return -1
                


            

