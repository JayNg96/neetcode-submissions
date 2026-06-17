class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        new_num = []

        for i in range(len(nums)):
            total = None
            exclude_itself = nums[:i] + nums[i+1:]
            for e in exclude_itself:
                if total is None:
                    total = e
                else:
                    total *= e
            new_num.append(total)

        return new_num