class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:           
        if self.stack:
            if val > self.stack[-1][1]:
                self.stack.append((val, self.stack[-1][1]))
            else:
                self.stack.append((val, val))
        else:
            self.stack.append((val, val))
        
    def pop(self) -> None:
        self.stack.pop()
        
    def top(self) -> int:
        print('top', self.stack[-1][0])
        return self.stack[-1][0] if self.stack else None

    def getMin(self) -> int:
        print('min', self.stack[-1][1])
        return self.stack[-1][1] if self.stack else None