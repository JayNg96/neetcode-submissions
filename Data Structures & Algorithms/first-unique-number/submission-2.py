class FirstUnique:

    def __init__(self, nums: List[int]):
        self.num_hashmap = defaultdict(int)
        for n in nums:
            self.num_hashmap[n] += 1

    def showFirstUnique(self) -> int:
        for num, count in self.num_hashmap.items():
            if count == 1:
                return num
        return -1

    def add(self, value: int) -> None:
        self.num_hashmap[value] += 1

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
