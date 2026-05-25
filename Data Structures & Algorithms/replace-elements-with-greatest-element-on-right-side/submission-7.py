class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightMax = -1
        for i in reversed(range(len(arr))):
            newRightMax = max(rightMax, arr[i])
            arr[i] = rightMax
            rightMax = newRightMax
        return arr