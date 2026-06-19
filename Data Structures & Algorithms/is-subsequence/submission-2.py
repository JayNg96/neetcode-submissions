class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        s_queue = deque()

        for string in s:
            s_queue.append(string)

        
        for string in t:
            if not s_queue:
                return True
            if string == s_queue[0]:
                s_queue.popleft()

        return False if s_queue else True

            