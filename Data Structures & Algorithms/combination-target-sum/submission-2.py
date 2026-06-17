class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums:
            return []

        result = []
        bag = []
        
        def _helper(index = 0):
            if sum(bag) == target:
                if bag not in result:
                    result.append(list(bag))
                else:
                    return

            if sum(bag) > target:
                return

            if index == len(nums):
                return

            bag.append(nums[index])
            _helper(index)
            bag.pop()
            _helper(index + 1)

        _helper()
        return result

