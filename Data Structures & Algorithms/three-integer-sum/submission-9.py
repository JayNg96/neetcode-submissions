class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        
        nums.sort()

        res = []
        
        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            while r > l:
                if nums[i] > 0:
                    break

                sum_three = nums[i] + nums[l] + nums[r]
                
                if sum_three > 0:
                    r -= 1
                elif sum_three < 0:
                    l += 1
                else:
                    summed_to_zero = [nums[i], nums[l], nums[r]]
                    if summed_to_zero not in res:
                        res.append(list([nums[i], nums[l], nums[r]]))
                    l += 1
                    r -= 1             


        return res
