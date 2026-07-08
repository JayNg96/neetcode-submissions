class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        
        s_queue = deque(s)
        
        for direction, amount in shift:
            for _ in range(amount):
                if direction == 0:
                    s = s_queue.popleft()
                    s_queue.append(s)
                else:
                    s = s_queue.pop()
                    s_queue.appendleft(s)

        new_s = ""
        while s_queue:
            new_s += s_queue.popleft()
        
        return new_s


