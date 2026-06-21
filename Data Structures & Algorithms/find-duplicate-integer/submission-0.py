class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        set_nums = set()

        for n in nums:
            if n in set_nums:
                return n
            else:
                set_nums.add(n)