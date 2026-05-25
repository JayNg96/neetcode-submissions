class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        maxCount = 0
        count = 0
        for i in nums:
            if i == 1:
                count+=1
                if count > maxCount:
                    maxCount = count
                continue
            else:
                count = 0
        return maxCount