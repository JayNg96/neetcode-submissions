class MinStack:

    def __init__(self):
        self.stack = []           # stores (value, current_min)
        
    def push(self, val: int) -> None:
        if not self.stack:
            current_min = val
        else:
            current_min = min(val, self.stack[-1][1])
        
        self.stack.append((val, current_min))
        
    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1][0] if self.stack else None   # or raise error
        
    def getMin(self) -> int:
        return self.stack[-1][1] if self.stack else None