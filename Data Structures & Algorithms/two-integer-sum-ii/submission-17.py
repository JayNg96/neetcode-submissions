class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while right > left:
            sum_of_left_n_right = numbers[left] + numbers[right]

            if sum_of_left_n_right > target:
                right -= 1
            elif sum_of_left_n_right < target:
                left += 1
            else:
                return [left+1, right+1]
        
                
        