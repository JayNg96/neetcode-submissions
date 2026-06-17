class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums:
            return []

        result = []
        bag = []

        def _helper(index = 0, total = 0):
            if total == target:
                result.append(list(bag))
                return

            if total > target:
                return

            if index == len(nums):
                return

            bag.append(nums[index])
            _helper(index, total + nums[index])
            bag.pop()
            _helper(index + 1, total)

            return result
        
        return _helper()

