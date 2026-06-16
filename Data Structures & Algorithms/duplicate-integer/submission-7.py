class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count_nums = {}

        for n in nums:
            if n not in count_nums:
                count_nums[n] = 1
            else:
                return True
        
        return False
