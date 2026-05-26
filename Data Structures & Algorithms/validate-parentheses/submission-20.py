class Solution:
    def isValid(self, s: str) -> bool:
        match = {
            "{":"}",
            "(":")",
            "[":"]"        
        }
        stack = []

        for i in s:
            if i in match:
                stack.append(i)
            else:
                if not stack or match.get(stack[-1]) != i:
                    return False
                stack.pop()

        return len(stack) == 0