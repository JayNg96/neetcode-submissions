class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        sorted_cars = sorted(zip(position, speed), reverse=True)
        stack = []

        for pos, spe in sorted_cars:
            time_to_target = (target - pos) / spe

            if stack and stack[-1] >= time_to_target:
                continue

            stack.append(time_to_target)
            
    
        print(stack)
        return len(stack)
