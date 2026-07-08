class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.q = deque()

    def next(self, val: int) -> float:
        if not self.q:
            self.q.append((val, val))
            return val / 1
        
        curr_max = self.q[-1][1]
        new_max = curr_max + val
        if len(self.q) == self.size:
            new_max -= self.q.popleft()[0]
        self.q.append((val, new_max))
        return new_max / len(self.q)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
