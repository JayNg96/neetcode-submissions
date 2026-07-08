class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        li_str = [w for w in s]

        for direction, distance in shift:
            
            for _ in range(distance):
                if direction == 0:
                    s = li_str.pop(0)
                    li_str.append(s)
                else:
                    s = li_str.pop()
                    li_str.insert(0, s)

        return "".join(li_str)