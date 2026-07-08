class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        num_freq = {}
        for n in nums:
            if n in num_freq:
                num_freq[n] += 1
            else:
                num_freq[n] = 1
        
        largest_n = -1
        for n, count_of_n in num_freq.items():
            if count_of_n == 1:
                largest_n = max(largest_n, n)
        
        return largest_n


            

