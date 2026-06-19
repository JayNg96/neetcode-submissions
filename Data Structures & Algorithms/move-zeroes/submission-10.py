class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        

        fast = 0
        slow = 0
        end_of_list = len(nums) - 1

        while fast < end_of_list:
            
            if nums[slow] != 0:
                slow += 1
                fast += 1

            if nums[fast] == 0 and fast < end_of_list:
                fast += 1
            
            if nums[slow] == 0 and nums[fast] > 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
            
            
            

            

