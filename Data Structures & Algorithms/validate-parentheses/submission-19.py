class Solution:
    def isValid(self, s: str) -> bool:
        match = {
            "{":"}",
            "(":")",
            "[":"]"        
        }
        stack = []

        for i in s:
            if i in match.keys():
                stack.append(i)
            else:
                if stack and match.get(stack[-1]) == i:
                    stack.pop()
                else:
                    return False
    
        return True if len(stack) == 0 else False