class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count_nums = {}

        for n in nums:
            if n not in count_nums:
                count_nums[n] = 1
            else:
                count_nums[n] += 1
        
        return any(x >= 2 for x in count_nums.values())
