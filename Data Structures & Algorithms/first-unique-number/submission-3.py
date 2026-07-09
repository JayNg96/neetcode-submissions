class FirstUnique:

    def __init__(self, nums: List[int]):
        self.cnt = Counter(nums)
        self.unique = {n: c for n, c in self.cnt.items() if c == 1}
        print(self.unique)


    def showFirstUnique(self) -> int:
        return -1 if not self.unique else next(v for v in self.unique.keys())

    def add(self, value: int) -> None:
        if value in self.unique:
            self.unique.pop(value)
        else:
            self.unique[value] = 1
        
# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
