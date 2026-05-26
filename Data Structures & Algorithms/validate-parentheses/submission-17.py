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
            elif i in match.values():
                if len(stack) > 0:
                    if match.get(stack[-1]) == i:
                        stack.pop()
                        continue
                    return False
                return False
    
        return len(stack) == 0