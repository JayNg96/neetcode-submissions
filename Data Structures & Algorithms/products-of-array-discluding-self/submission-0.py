class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        new_nums = []

        for i in range(len(nums)):
            temp = nums.pop(i)
            new_nums.append(math.prod(nums))
            nums.insert(i, temp)

        return new_nums