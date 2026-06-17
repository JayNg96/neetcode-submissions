class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return nums

        bucket = [0,0,0]

        for n in nums:
            bucket[n] += 1

        index = 0
        for i in range(len(bucket)):
            for _ in range(bucket[i]):
                nums[index] = i
                index+=1

