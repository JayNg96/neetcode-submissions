class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        if len(nums) == 1:
            return 1

        num_set = set(nums)
        max_consecutive = 0
        
        for num in nums:
            if num - 1 not in num_set: 
                consecutive = 1
                while num + consecutive in num_set:
                    consecutive += 1
                max_consecutive = max(max_consecutive, consecutive)
        
        return max_consecutive