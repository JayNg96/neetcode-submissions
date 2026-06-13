class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        bag = []

        def _dfs(index: int):
            if index == len(nums):
                result.append(list(bag))
                return

            bag.append(nums[index])
            _dfs(index + 1)

            bag.pop()
            _dfs(index + 1)

        _dfs(0)
        return result
