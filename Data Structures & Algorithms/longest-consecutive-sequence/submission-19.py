class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
            
        cons, max_cons = 1, 0
        nums = sorted(set(nums))
        print(nums)
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 1:
                cons += 1
            else:
                if cons > max_cons:
                    max_cons = cons
                cons = 1
            
        
        return max(cons, max_cons)