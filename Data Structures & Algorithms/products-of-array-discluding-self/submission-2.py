class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        new_nums = []

        for i in range(len(nums)):
            exclude_itself = math.prod(nums[:i] + nums[i+1:])
            new_nums.append(exclude_itself)

        return new_nums