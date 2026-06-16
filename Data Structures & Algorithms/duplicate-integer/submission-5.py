class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count_nums = {}

        for n in nums:
            if n not in count_nums:
                count_nums[n] = 1
            else:
                count_nums[n] += 1
        
        return any(count >= 2 for count in count_nums.values())
