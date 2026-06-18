class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        num_queue = {y: x + 1 for x, y in enumerate(numbers)}
        print(num_queue)
        for i in range(len(numbers)):
            print(target - numbers[i])
            if target - numbers[i] in num_queue:
                return [i + 1, num_queue.get(target - numbers[i])]

        