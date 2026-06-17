class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums:
            return []

        result = []
        bag = []

        def helper(index = 0, total = 0):
            if total == target:
                result.append(list(bag))
                return

            if total > target:
                return

            if index == len(nums):
                return

            bag.append(nums[index])
            helper(index, total + nums[index])
            bag.pop()
            helper(index + 1, total)

        helper()
        return result

