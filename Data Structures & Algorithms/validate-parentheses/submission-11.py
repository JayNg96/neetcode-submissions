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
            elif i in match.values():
                if len(stack) > 0:
                    if match.get(stack[-1]) == i:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        
        print(stack)
        return True if len(stack) == 0 else False