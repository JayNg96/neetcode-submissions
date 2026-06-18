class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        target_first_val = None
        for i in range(len(numbers)):
            if target_first_val is None:
                if target - numbers[i] in numbers:
                    target_first_val = i
            else:
                if numbers[i] + numbers[target_first_val] == target:
                    return [target_first_val + 1, i + 1]
                

