from collections import deque
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()

        for t in tokens:
            if t.isalnum() or t.startswith('-') and t[1:].isdigit():
                stack.append(int(t))
            else:
                second_num = stack.pop()
                first_num = stack.pop()
                if t == "+":
                    stack.append(first_num + second_num)
                elif t == "-":
                    stack.append(first_num - second_num)
                elif t == "*":
                    stack.append(first_num * second_num)
                else:
                    stack.append(int(first_num / second_num))
        return stack[0]