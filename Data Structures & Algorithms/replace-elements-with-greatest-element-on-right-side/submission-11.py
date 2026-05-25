class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        right_max = -1
        for i in reversed(range(len(arr))):
            arr[i], right_max = right_max, max(right_max, arr[i])
        return arr