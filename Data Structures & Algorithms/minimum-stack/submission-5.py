from collections import deque

class MinStack:

    def __init__(self):
        self.stack = deque([])

    def push(self, val: int) -> None:
        self.stack.append(val)
        
    def pop(self) -> None:
        self.stack.pop()
         
    def top(self) -> int:
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        print("min:",min(self.stack))
        return min(self.stack)