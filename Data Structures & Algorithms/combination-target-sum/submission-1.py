from typing import List

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        bag = []

        def _dfs(index=0, current_sum=0): 
            # print(bag)
            # print(current_sum)
            if current_sum == target:
                # print('current_sum == target:', bag)
                result.append(bag.copy())
                return 

            if index == len(nums) or current_sum > target:
                return
            
            bag.append(nums[index])
            current_sum += nums[index]
            _dfs(index, current_sum)

            bag.pop()
            current_sum -= nums[index]
            _dfs(index + 1, current_sum)
            
        _dfs()
        return result